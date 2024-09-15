# From-Images-to-Emissions
# Rice Straw Burning Detection & CO2 Emissions Estimation
## Overview
This project focuses on developing a real-time computer vision model using YOLOv8 and PySpark to detect rice straw burning in agricultural fields. Rice straw burning is a major source of CO2 emissions in Vietnam, and this tool aims to improve the understanding and prediction of environmental impact. By enhancing predictive models, this project enables a more comprehensive approach to environmental monitoring.

## Motivation
Agriculture in Vietnam is the backbone of the economy, and rice farming is one of the most crucial industries. However, the by-products of rice farming, particularly rice straw, are often burned, leading to significant CO2 emissions. Monitoring and predicting these emissions is a challenging task that requires considerable resources for data collection across vast regions.

This project is a pilot initiative aimed at addressing the environmental impact of rice straw burning in a scalable and efficient manner. As an ongoing effort, we plan to improve and expand the model to cover larger areas, refining its accuracy and performance.

## Data Collection & Labeling
The model relies heavily on high-quality, labeled images of rice fields. Over 1,000 images have been collected and classified to improve model accuracy. Each image is manually labeled to indicate the presence of burning straw, and this information is used to train the model. The goal is to ensure that the model can not only detect instances of burning but also estimate the resulting CO2 emissions in real-time.

## Model Architecture & Training
We employ YOLOv8 for object detection due to its balance of speed and accuracy, which is critical for real-time applications. The model is labeled using ** Roboflow **, leveraging distributed computing to handle large datasets and improve scalability. Currently, the model achieves 60% accuracy, with ongoing efforts to increase this through further training and hyperparameter tuning.

## Spatial Analysis
In addition to detection, the model is capable of performing real-time spatial analysis, mapping detected burning events back onto a larger geographical region. By merging image outputs and geospatial data, the model creates a broader picture of emissions across large rice-growing areas. This provides valuable insight into how agricultural practices affect air quality and contributes to climate change mitigation efforts.

## Future Directions
As this is a pilot project, there are several areas of planned development:

Expand data collection to cover more regions and varying conditions.
Improve model accuracy through more robust training and testing with diverse datasets.
Integrate predictive analytics for estimating long-term environmental impact based on real-time detection data.
