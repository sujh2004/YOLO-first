from ultralytics import YOLO

model = YOLO('yolov8n.yaml')

model = YOLO('yolov8n.pt')  # 加载YOLOv8的Nano模型（体积最小）

model.predict('bus.jpg',save=True)
model.predict('image1.jpg',save=True)
model.predict('image2.jpg',save=True)
