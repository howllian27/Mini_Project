import os
import numpy as np
import pandas as pd
import json
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.preprocessing import image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Load the pre-trained ResNet50 model for feature extraction
cnn_model = keras.applications.ResNet50(weights='imagenet', include_top=False, pooling='avg')

frame_names = []


# Function to check if the JSON file is empty or newly created
def is_json_file_empty(file_path):
    try:
        return os.stat(file_path).st_size == 0
    except FileNotFoundError:
        return True

# Function to initialize the JSON file if necessary
def initialize_json_file(file_path):
    if is_json_file_empty(file_path):
        with open(file_path, 'w') as f:
            f.write('{\n')


# Function to safely append data to the JSON file
def append_to_json_file(file_path, frame_identifier, features):
    # Convert the entire NumPy array to a list for JSON serialization
    features_list = features.flatten().tolist()
    
    with open(file_path, 'r+') as f:
        # Move to the end of the file to check if it's empty or has content
        f.seek(0, os.SEEK_END)
        pos = f.tell()
        if pos > 2:
            # Not empty, move back to overwrite the last newline and closing brace
            f.seek(pos - 2)
            # Write a comma if this isn't the first entry
            f.write(',\n')
        else:
            # Empty, write the opening brace
            f.write('{\n')
        
        # Create the JSON entry with the full list of features
        json_entry = json.dumps({frame_identifier: features_list})
        # Remove the curly braces from the individual JSON entry
        json_entry = json_entry[1:-1]
        
        # Append the new data and close the JSON object
        f.write(json_entry)
        f.write('\n}')


def extract_features(img_path):
    """Extract features from a single image without appending to JSON."""
    img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    img_array = keras.preprocessing.image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = keras.applications.resnet50.preprocess_input(expanded_img_array)
    features = cnn_model.predict(preprocessed_img)
    return features

def process_video(video_frames_folder, video_identifier):
    """Process a video given its folder containing frames and calculate mean feature vector."""
    frame_features = []
    for frame in sorted(os.listdir(video_frames_folder)):
        frame_path = os.path.join(video_frames_folder, frame)
        print(frame_path)
        features = extract_features(frame_path)
        frame_features.append(features)
    if frame_features:  # Ensure there are frames processed
        mean_feature_vector = np.mean(np.array(frame_features).squeeze(), axis=0)
        append_to_json_file('frame_features.json', video_identifier, mean_feature_vector)
        return mean_feature_vector
    return None

def load_data_and_labels(videos_path, scores_file):
    """Load mean video features and intensity scores."""
    initialize_json_file('frame_features.json')  # Ensure JSON file is initialized
    scores_df = pd.read_csv(scores_file)
    intensity_scores_dict = pd.Series(scores_df.intensity_score.values, index=scores_df.video_frame).to_dict()
    
    video_features = []
    intensity_scores = []

    filtered_vid_lst = os.listdir(videos_path)[320:]

    for video_folder in filtered_vid_lst:
        video_folder_path = os.path.join(videos_path, video_folder)
        if os.path.isdir(video_folder_path):
            mean_feature_vector = process_video(video_folder_path, video_folder)
            if mean_feature_vector is not None:
                video_features.append(mean_feature_vector)
                # Assuming intensity score is associated with the video, not individual frames
                if video_folder in intensity_scores_dict:
                    intensity_scores.append(intensity_scores_dict[video_folder])
    
    return np.array(video_features), np.array(intensity_scores)


# Define the LSTM model for processing sequences of features
def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(units=256, input_shape=input_shape, return_sequences=True),
        LSTM(units=128),
        Dense(units=64, activation='relu'),
        Dense(units=1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

initialize_json_file('frame_features.json')

# Main script
videos_path = "videos/"
scores_file = "intensity_scores.csv"

# Load data
video_features, intensity_scores = load_data_and_labels(videos_path, scores_file)

# Save video_features and intensity_scores to disk
np.save('video_features.npy', video_features)
np.save('intensity_scores.npy', intensity_scores)

# Load video_features and intensity_scores from disk
video_features_loaded = np.load('video_features.npy', allow_pickle=True)
intensity_scores_loaded = np.load('intensity_scores.npy', allow_pickle=True)
frames_names_array = np.array(frame_names)
cnn_model.summary()
np.save('frame_names.npy', frames_names_array)

# Since videos have different lengths, we need to pad sequences
video_features_padded = keras.preprocessing.sequence.pad_sequences(video_features_loaded, padding='post', dtype='float32')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(video_features_padded, intensity_scores_loaded, test_size=0.2, random_state=42)

# Create and train the LSTM model
input_shape = (X_train.shape[1], X_train.shape[2])
model = create_lstm_model(input_shape)
model.fit(X_train, y_train, epochs=10, validation_split=0.2)
model.save('most_replayed_model.keras')

# Evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
