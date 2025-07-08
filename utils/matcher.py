import numpy as np

def get_centroid(box):
    x1, y1, x2, y2, _ = box
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def match_players(detections1, detections2):
    all_matches = []

    for frame1, frame2 in zip(detections1, detections2):
        matches = []
        for i, box1 in enumerate(frame1):
            min_dist = float('inf')
            match_idx = -1
            for j, box2 in enumerate(frame2):
                dist = np.linalg.norm(np.array(get_centroid(box1)) - np.array(get_centroid(box2)))
                if dist < min_dist:
                    min_dist = dist
                    match_idx = j
            if match_idx != -1:
                matches.append((i, match_idx))
        all_matches.append(matches)

    return all_matches
