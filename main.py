from utils.detector import detect_players
from utils.matcher import match_players
import cv2
import os

# Paths
video1_path = 'data/broadcast.mp4'
video2_path = 'data/tacticam.mp4'

# Detect players
print("[INFO] Detecting players...")
detections1 = detect_players(video1_path)
detections2 = detect_players(video2_path)

# Match across cameras
print("[INFO] Matching players across cameras...")
matched_ids = match_players(detections1, detections2)

# Draw + Export sample matched detections
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Optional: Visual confirmation (only first 100 frames)
cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out1 = cv2.VideoWriter(f'{output_dir}/broadcast_labeled.mp4', fourcc, 30.0, (int(cap1.get(3)), int(cap1.get(4))))
out2 = cv2.VideoWriter(f'{output_dir}/tacticam_labeled.mp4', fourcc, 30.0, (int(cap2.get(3)), int(cap2.get(4))))

frame_num = 0
while cap1.isOpened() and cap2.isOpened() and frame_num < len(matched_ids):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1 or not ret2:
        break

    matches = matched_ids[frame_num]
    for (i, j) in matches:
        if i < len(detections1[frame_num]):
            x1, y1, x2, y2, _ = detections1[frame_num][i]
            cv2.rectangle(frame1, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.putText(frame1, f'ID:{i}', (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        if j < len(detections2[frame_num]):
            x1, y1, x2, y2, _ = detections2[frame_num][j]
            cv2.rectangle(frame2, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame2, f'ID:{i}', (int(x1), int(y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out1.write(frame1)
    out2.write(frame2)
    frame_num += 1

cap1.release()
cap2.release()
out1.release()
out2.release()
print("[INFO] Done! Output saved in /output")
