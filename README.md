# Building a Proof-of-Concept AI-Powered Video Analytics Engine for Content Creation   

## About
This project focuses on developing an AI-powered analytics engine that leverages deep learning to analyze video content. The goal is to extract meaningful insights that can help content creators optimize their videos for better viewer engagement and retention. The engine uses several neural network models to predict viewer engagement metrics based on visual and textual features extracted from the videos.


1. [Data Extraction & Visualisation](https://github.com/howllian27/Mini_Project/tree/main/src/data_collection)
   - [Exploratory Data Analysis](https://github.com/howllian27/Mini_Project/tree/main/src/data_collection/data_visualisation.ipynb)
2. [Model Training for Predicting View Count](https://github.com/howllian27/Mini_Project/blob/main/src/model_trainings/view_count_model.ipynb)
3. [Model Training for Predicting Most Replayed Segments](https://github.com/howllian27/Mini_Project/blob/main/src/model_trainings/most_replayed_model.py)
4. [Saved Model for Predicting View Count](https://github.com/howllian27/Mini_Project/blob/main/models/view_count_model.pth)
5. [Saved Model for Predicting Most Replayed Segments](https://github.com/howllian27/Mini_Project/blob/main/models/most_replayed_model.keras)
6. [Compiled Data](https://github.com/howllian27/Mini_Project/tree/main/data)
   
  
## Contributors

| Name                | Contributions                                                          |
| ------------------- | ---------------------------------------------------------------------- |
| Chan Hin Wai Howell | Machine Learning Models, Exploratory Data Analysis, Problem Definition |
| Lee Ern Qi Eunice   | Machine Learning Models, Exploratory Data Analysis, Problem Definition |
| Bryan Tao           | Exploratory Data Analysis, Data Preparation & Cleaning                 |

## Problem Definition

- Objective: To create a tool that can predict viewer engagement metrics such as view counts and watch duration based on the content of the videos.
- Challenge: Handling high-dimensional data and designing a model that accurately reflects viewer preferences.

## Algorithm Overview

1. **Initialization**: Set up the processing environment and video frame storage directory.
2. **Video ID Processing**: Loop through each video ID to process video content.
3. **Stream Setup**: Use CamGear to stream video content, handling stream failures with a retry mechanism.
4. **Frame Rate Detection**: Automatically determine and verify the video's frame rate for consistent frame extraction.
5. **Frame Extraction**: Capture and save video frames at predefined intervals to the storage directory.
6. **Metadata Collection**: Fetch video metadata via YouTube's API for each video.
7. **Feature Extraction**:
   - Utilize a pre-trained ResNet50 model to extract visual features from frames.
   - Process video titles for vocabulary embeddings using a sentence transformer.
8. **Feature Aggregation**: Compile frame-level features into a mean feature vector and serialize to JSON.
9. **Machine Learning Pipeline**:
   - Load and preprocess data for model input.
   - Use LSTM neural networks to predict intensity scores for video frames.
   - Apply a custom PyTorch neural network model to estimate video view counts.
   - Integrate LSTM and PyTorch model outputs, incorporating L1 regularization and custom loss functions during training.
10. **Model Evaluation**: Assess model performance with Mean Squared Error (MSE) on a test dataset.
11. **Output Synthesis**: Combine frame-level intensity scores with predicted view counts into a comprehensive analytical report.
12. **Finalization**: Save model parameters and generate output for end-user interpretation.
13. **Cleanup**: Conduct final housekeeping to reset the environment for subsequent analyses.

## Models Used

### LSTM Neural Network
- **Usage**: The LSTM (Long Short-Term Memory) neural network is utilized to analyze temporal sequences of video frames to predict intensity scores. This model excels at understanding the dynamics and progression within video content, capturing both short-term and long-term patterns. It is particularly effective in predicting metrics that depend on the sequence of events in the video, such as viewer engagement and reaction over time.
- **Architecture**: The LSTM model comprises two LSTM layers followed by dense layers. The first LSTM layer with 256 units returns sequences to capture temporal dependencies, feeding into another 128-unit LSTM layer. This setup ensures deep feature extraction from the sequence data. The subsequent dense layers with ReLU activation function aid in non-linear transformation, culminating in a single unit output that predicts the intensity score.

### Custom PyTorch Neural Network for Predicting View Count
- **Usage**: This custom neural network built with PyTorch is designed to predict view counts based on the aggregated features of the video content, including visual features from frames and metadata like titles. The model predicts potential popularity by analyzing the extracted features, which correlate visual content characteristics with historical view count data.
- **Architecture**: The network architecture includes:
  - **Input Layers**: Separate input layers for different types of features (vocab size, video features, title text), ensuring diverse data sources are effectively integrated.
  - **Hidden Layers**: A series of linear layers and dropout layers to prevent overfitting. The first set of layers maps high-dimensional input to a hidden space, followed by a concatenation layer that combines all features into a unified representation. Subsequent layers distill this combined feature set to predict the view count.
  - **Output Layer**: A single output layer that provides the estimated view count. 

### ResNet50 for Feature Extraction
- **Usage**: ResNet50, a powerful convolutional neural network pre-trained on ImageNet, is employed for feature extraction from video frames. This model captures a broad array of visual features such as textures, objects, and scene configurations, which are crucial for understanding content quality and viewer preferences.
- **Configuration**: The model is used in a 'feature extraction' mode where the top classification layer is removed, allowing us to obtain a rich feature vector from the 'average pooling' layer. These features represent the distilled essence of the video frames, feeding into further predictive models.

### Loss Functions
- **Custom Loss Function**: To tailor the training process to our specific needs, a custom loss function is implemented. This function penalizes predictions based on their deviation from true values, with added penalties for negative predictions and highly inaccurate predictions, encouraging the model to focus on plausible and accurate outputs.
- **L1 Regularization**: Incorporated into the custom model training to enhance generalization by penalizing the absolute value of the weights. This encourages sparsity in the model parameters, potentially leading to simpler and more interpretable models.

These models work in tandem within a comprehensive machine learning pipeline, where each component plays a crucial role in transforming raw video data into actionable insights for content creators.

## Conclusion
- Developed functional video analytics models capable of predicting viewer engagement metrics with a moderately high degree of accuracy.
- Demonstrated the effectiveness of feature normalization and custom loss functions in enhancing model performance.

## What did we learn from this project?
- Technical Skills: Gained proficiency in PyTorch and TensorFlow, mastering complex model architectures and data processing pipelines.
- Analytical Skills: Enhanced our ability to translate business problems into data-driven solutions, improving our analytical and problem-solving skills.

## Collaborating

Checkout to a new feature branch when making changes.

```bash
# make sure you are on main
git checkout -b <name>/<description>

# integrate latest changes from collaborators on your feature branch
git pull
git rebase origin/main
```

Follow semantic commit messages when making commits: 📃 [Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)

```bash
git commit -m "<type>: <description>"
```
## References

- <https://www.kaggle.com/datasets/vicomtehorace/most-replayed-with-transcription-youtube-video>
- <https://arxiv.org/abs/1512.03385>
- <https://pytorch.org/docs/stable/index.html>
- <https://www.tensorflow.org/api_docs> 
- <https://developers.google.com/youtube/v3>
- <https://abhitronix.github.io/vidgear/v0.3.2-stable/>
- <https://medium.com/swlh/heres-exactly-how-much-money-we-earned-from-1-3-million-youtube-views-fd80aae48212>
- <https://medium.com/@shane_barker/top-earning-youtube-channels-and-their-success-secrets-a06e1954a504>
