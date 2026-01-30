"""
Training script for YOLOv8-based power infrastructure fault detection.
This script trains an object detection model on UAV imagery.
"""

import os
from ultralytics import YOLO


def main():
    """
    Main training function.
    """

    # -----------------------------
    # 1. Load YOLOv8 model
    # -----------------------------
    # Using a pretrained YOLOv8 small model for transfer learning
    model = YOLO("yolov8s.pt")

    # -----------------------------
    # 2. Dataset configuration
    # -----------------------------
    # Path to dataset.yaml file
    data_config = os.path.join("data", "data.yaml")

    # -----------------------------
    # 3. Train the model
    # -----------------------------
    model.train(
        data=data_config,
        epochs=50,
        imgsz=640,
        batch=8,
        project="runs",
        name="powerline_fault_detection"
    )


if __name__ == "__main__":
    main()
