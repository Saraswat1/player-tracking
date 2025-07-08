# Player Re-Identification Assignment Report

## 🔍 Approach and Methodology

This project performs **player detection and re-identification across two video views**: a broadcast view and a tacticam (top) view. The pipeline is divided into two main stages:

1. **Detection**:
   - We use a custom-trained **YOLOv8 model** (`best.pt`) to detect objects labeled as `player`, `goalkeeper`, and `referee`.
   - Each frame is passed to the model, and bounding boxes are extracted using `results[0].boxes.xyxy`.

2. **Re-Identification**:
   - To match players across views, we use a **centroid-based matching** strategy.
   - For each frame, we compute the centroids of detected bounding boxes in both videos and match players based on the shortest Euclidean distance.

Finally, annotated videos (`broadcast_labeled.mp4` and `tacticam_labeled.mp4`) are generated to visually confirm matching results.

---

## 🧪 Techniques Tried and Their Outcomes

- **YOLOv8 Detection**:
  - The model was effective in detecting players with good accuracy across varying angles.
  - Average inference time was ~900ms per frame.

- **Centroid-Based Matching**:
  - This simple method worked reasonably well in frames where the number of players and positions were consistent.
  - It sometimes struggled when players overlapped or when detection counts varied between views.

---

## ⚠️ Challenges Encountered

- **Detection Mismatches**:
  - Differences in camera angle caused varying detections — some players detected in one view but not the other.

- **ID Drift**:
  - Since the matching algorithm does not persist identity over time, it may mismatch IDs across frames.

- **Computation Time**:
  - Inference is relatively slow (~1s/frame), which can be improved using a GPU or optimizing the model.

---

## 🚧 Incomplete / Future Work

- **Temporal Consistency**:
  - Currently, the matching is done frame-by-frame. Using **tracking (e.g., DeepSORT)** can improve ID consistency.

- **Visual Embeddings**:
  - Using **deep feature embeddings** from a Re-ID model (e.g., OSNet) would result in more robust matching.

- **Scalability**:
  - This prototype is tested on 100 frames. For full-game analysis, optimization and batch processing would be needed.

---

## ✅ Summary

Despite some limitations, this submission demonstrates a working end-to-end system for detecting and matching players across views. The outputs (`broadcast_labeled.mp4` and `tacticam_labeled.mp4`) show proof of concept. With additional time and compute, the system can be made more robust using advanced matching and tracking techniques.
