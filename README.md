# **Emotion and Age-Based Music Recommendation System**

## **Introduction**

In today's fast-paced world, music provides emotional support and relaxation. However, selecting music that aligns with one’s mood and preferences can be challenging due to the vast array of choices and the variability in musical tastes across different age groups. This project addresses this challenge by developing a software solution that integrates **emotion and age recognition** to offer a more empathetic and customized music selection, thereby enhancing the overall user experience.

## **Objectives**

- **Emotion Recognition**: Develop a model to accurately recognize and interpret a user's emotional state.
- **Age Detection**: Implement an age estimation mechanism to accurately gauge the user's age.
- **Music Personalization**: Use emotion and age recognition data to curate personalized music playlists.
- **Real-Time Processing**: Ensure real-time processing and analysis of facial expressions for immediate music playlist generation.

## **Technologies Used**

- **Datasets**: 
  - **UTK**: For age and facial attribute analysis.
  - **Raf-DB**: For emotion recognition.

- **Machine Learning Models**:
  - **Convolutional Neural Networks (CNN)**: Used for detecting emotions and estimating age.
  - **WideResNet**: Specifically utilized for age estimation.

- **Techniques**:
  - **Data Augmentation**: To enhance model robustness.
  - **Dropout Regularization**: To prevent overfitting.
  - **Early Stopping**: To avoid overfitting and ensure model generalization.

- **Frontend Development**:
  - **HTML & CSS**: For creating interactive and user-friendly interfaces.

- **Backend Development**:
  - **Flask**: For backend logic and RESTful API creation.
  - **RESTful APIs**: For communication between frontend and backend.

## **Methodology**

1. **Dataset Acquisition**: 
   - Sourced from Kaggle, using UTK and Raf-DB datasets to cover diverse real and synthetic content.

2. **Model Development**:
   - **Develop separate models** for age and emotion detection using CNN and WideResNet.
   - Apply **data augmentation**, **dropout regularization**, and **early stopping**.

3. **Model Integration**:
   - Create an **ensemble model** optimized through iterative training and refinement of composition strategies.

4. **Evaluation**:
   - Partition dataset into training, validation, and test sets.
   - Use metrics such as **accuracy**, **precision**, **recall**, and **F1-score**.
   - Visualize performance with **confusion matrices**.
   - Conduct **robustness testing** across various datasets and conditions.

5. **Frontend and Backend Development**:
   - **Frontend**: Design interfaces using HTML and CSS for user interaction.
   - **Backend**: Implement Flask and RESTful APIs to handle real-time face analysis and music recommendation.

## **Results and Conclusions**

The system’s effectiveness was assessed using **accuracy**, **precision**, **recall**, and **F1-score** metrics. The **CNN for emotion detection** and **WideResNet for age estimation** demonstrated effective real-time video feed processing. The use of **pre-trained weights** reduced computational overhead while maintaining high accuracy. **Flask** provided a user-friendly web interface for seamless user interaction and real-time music recommendations based on emotional and age insights.

## **Scope for Future Work**

- **Multimodal Detection**: Incorporate **voice tone analysis** and **body language interpretation** for a comprehensive mood and emotional state understanding.
- **Dataset Expansion**: Include a wider range of emotional expressions across various cultures and demographics to enhance accuracy and inclusiveness.
- **Real-Time Feedback**: Implement a feedback mechanism for users to rate music recommendations, refining future suggestions.
- **Cross-Platform Integration**: Develop **APIs** for integration with multiple streaming platforms and social media for seamless access to personalized music playlists.

