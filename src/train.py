"""
train.py

This script trains a YOLOv8 model to detect faults in
overhead power transmission infrastructure using UAV imagery.
"""

from ultralytics import YOLO
import os


def main():
    """
    Main training pipeline.
    """
    print("Starting YOLOv8 training pipeline...")

    # Load a pretrained YOLOv8 model
    model = YOLO("yolov8n.pt")

    # Path to dataset configuration file
    data_config = os.path.join("data", "dataset.yaml")

    # Train the model
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
