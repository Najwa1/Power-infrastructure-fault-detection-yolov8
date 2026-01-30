**Automated Power Infrastructure Fault Detection using YOLOv8
Overview**

Inspection of power transmission infrastructure is critical for maintaining a reliable electricity supply. Traditionally, this inspection is done manually or with helicopters, which is expensive, slow, and sometimes dangerous.

In this project, we will build an end-to-end computer vision system that automatically detects faults in power infrastructure from aerial (UAV) images using YOLOv8.



This repository is written as a learning-first, engineering-focused walkthrough.



**Dataset Structure**



The dataset is organized following YOLOv8 conventions:



data/

├── images/

│   ├── train/

│   └── val/

├── labels/

│   ├── train/

│   └── val/

├── raw/

├── processed/

└── data.yaml



The data.yaml file defines training and validation paths and class names.



