import pandas as pd
data = pd.read_json("data.json")

new_rows = []

# Function to find intensity score for a given time
def find_intensity_score(items, current_time):
    for item in items:
        start = item['startMillis']
        end = start + item['durationMillis']
        if start <= current_time < end:
            return item['intensityScoreNormalized']
    return None  # Return None or a default value if no matching interval is found

for index, row in data.iterrows():
    video_id = row['id']
    items = row['items']
    
    # Determine the total duration
    if items:
        total_duration = max(item['startMillis'] + item['durationMillis'] for item in items)
    else:
        continue  # Skip if there are no items
    
    # Iterate through each 5-second interval
    for current_time in range(0, total_duration, 5000):
        frame_no = current_time // 5000
        video_frame = f"{video_id}_{frame_no}"
        intensity_score = find_intensity_score(items, current_time)
        
        # Append the new row to the list
        new_rows.append({'video_frame': video_frame, 'intensity_score': intensity_score})

# Create a new DataFrame from the list of new rows
new_df = pd.DataFrame(new_rows)

# Display the new DataFrame
new_df.to_csv("intensity_scores.csv", index=False)