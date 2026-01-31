**Automated Power Infrastructure Fault Detection using YOLOv8
Overview**

Inspection of power transmission infrastructure is critical for maintaining a reliable electricity supply. Traditionally, this inspection is done manually or with helicopters, which is expensive, slow, and sometimes dangerous.

In this project, we will build an end-to-end computer vision system that automatically detects faults in power infrastructure from aerial (UAV) images using YOLOv8.



**Dataset**

This project uses a sample from InsPLAD, a Power Line Asset Inspection Dataset and Benchmark containing 10,607 high-resolution Unmanned Aerial Vehicles color images. It is the first large real-world dataset and benchmark for power line asset inspection with multiple components and defects for various computer vision tasks (*André Luis et al, 2023*).



Only a small subset of the dataset is included in this repository for demonstration purposes.

The full dataset is publicly available at **https://github.com/andreluizbvs/InsPLAD/.**



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





