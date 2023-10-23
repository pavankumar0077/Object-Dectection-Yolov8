import argparse
from ultralytics import YOLO

# Define a command-line argument for the source
parser = argparse.ArgumentParser(description="YOLO Prediction Script")
parser.add_argument("--source", required=True, help="Input source for YOLO prediction")

# Parse the command-line arguments
args = parser.parse_args()

# Create a YOLO model
model = YOLO("yolov8n.pt")

# Perform prediction on the provided source
results = model.predict(source=args.source, show=True)
print(results)
