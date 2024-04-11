# Building a Proof-of-Concept AI-Powered Video Analytics Engine for Content Creation   

## About
This project focuses on developing an AI-powered analytics engine that leverages deep learning to analyze video content. The goal is to extract meaningful insights that can help content creators optimize their videos for better viewer engagement and retention. The engine uses several neural network models to predict viewer engagement metrics based on visual and textual features extracted from the videos.


1. [Data Extraction & Visualisation](https://github.com/howllian27/Mini_Project/tree/main/src/data_collection)
2. [Model Training for Predicting View Count](https://github.com/howllian27/Mini_Project/blob/main/src/model_trainings/view_count_model.ipynb)
3. [Model Training for Predicting Most Replayed Segments](https://github.com/howllian27/Mini_Project/blob/main/src/model_trainings/most_replayed_model.py)
4. [Saved Model for Predicting View Count](https://github.com/howllian27/Mini_Project/blob/main/models/view_count_model.pth)
5. [Saved Model for Predicting Most Replayed Segments](https://github.com/howllian27/Mini_Project/blob/main/models/most_replayed_model.keras)
6. [Compiled Data](https://github.com/howllian27/Mini_Project/tree/main/data)
   
  
## Contributors

- [Chan Hin Wai Howell](https://github.com/howllian27)
- [Lee Ern Qi Eunice](https://github.com/XeuniceX)
- [Bryan Tao](https://github.com/bryan0021)

## Problem Definition

- Objective: To create a tool that can predict viewer engagement metrics such as view counts and watch duration based on the content of the videos.
- Challenge: Handling high-dimensional data and designing a model that accurately reflects viewer preferences.

## Models Used
- Custom Neural Network Model: Built with PyTorch, this model integrates feature extraction and prediction layers to forecast engagement metrics.
- LSTM Model: Used to analyze temporal patterns in video frame sequences to predict engagement over time.
  
## Conclusion
- Developed functional video analytics models capable of predicting viewer engagement metrics with a moderately high degree of accuracy.
- Demonstrated the effectiveness of feature normalization and custom loss functions in enhancing model performance.

## What did we learn from this project?
- Technical Skills: Gained proficiency in PyTorch and TensorFlow, mastering complex model architectures and data processing pipelines.
- Analytical Skills: Enhanced our ability to translate business problems into data-driven solutions, improving our analytical and problem-solving skills.

## References

- <https://www.kaggle.com/datasets/vicomtehorace/most-replayed-with-transcription-youtube-video>
- <https://arxiv.org/abs/1512.03385>
- <https://pytorch.org/docs/stable/index.html>
- <https://www.tensorflow.org/api_docs> 
- <https://developers.google.com/youtube/v3>
- <https://abhitronix.github.io/vidgear/v0.3.2-stable/>
- <https://medium.com/swlh/heres-exactly-how-much-money-we-earned-from-1-3-million-youtube-views-fd80aae48212>
- <https://medium.com/@shane_barker/top-earning-youtube-channels-and-their-success-secrets-a06e1954a504>
