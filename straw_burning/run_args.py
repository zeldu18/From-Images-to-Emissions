

import argparse
from ultralytics import YOLO
import torch

DEFAULT_MODEL_PATH = "best.pt"

def main(args):
    # Initialize YOLO model
    model = YOLO(args.model)

    # Determine device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Using device: {device}')

    # Process arguments
    if args.image_path:
        # Process single image
        model(args.image_path, save=True, show=True, conf=args.confidence, iou=args.iou, show_labels=args.show_labels, show_boxes=args.show_boxes)
    elif args.image_folder:
        # Process images in a folder
        model(args.image_folder, save=True, show=False, labels=args.label)
    else:
        print("Please provide either an image path or an image folder path.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLO Object Detection")
    parser.add_argument("--image-path", type=str, help="Path to the image for detection")
    parser.add_argument("--image-folder", type=str, help="Path to the folder containing images for detection")
    parser.add_argument("--confidence", type=float, default=0.1, help="Confidence threshold for detection")
    parser.add_argument("--iou", type=float, default=0.45, help="IOU threshold for detection")
    parser.add_argument("--show-labels", action="store_true", help="Whether to show labels")
    parser.add_argument("--show-boxes", action="store_true", help="Whether to show boxes")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL_PATH, help=f"Path to the YOLO model file (default: {DEFAULT_MODEL_PATH})")
    args = parser.parse_args()
    main(args)