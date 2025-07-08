from ultralytics import YOLO

# Load trained YOLOv8 model
model = YOLO("models/best.pt")

def detect_players(video_path):
    import cv2

    cap = cv2.VideoCapture(video_path)
    all_detections = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        detections = []
        for box, conf in zip(results.boxes.xyxy, results.boxes.conf):
            x1, y1, x2, y2 = box[:4].cpu().numpy()
            conf = float(conf.cpu().numpy())
            detections.append([x1, y1, x2, y2, conf])
        
        all_detections.append(detections)

    cap.release()
    return all_detections
