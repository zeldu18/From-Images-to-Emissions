from ultralytics import YOLO
import torch

model = YOLO("best.pt")
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# without label
model(
    "test.jpg",
    save=True,
    show=True,
    conf=0.1,
    iou=0.45,
    show_labels=False,
    show_boxes=False,
)

#  run on gpu
# model = YOLO('best.pt')

# model.export(format='onnx')
