# Player Tracking & Re-Identification (Cross-Camera)

This project is a solution to the Player Re-Identification assignment provided by Liat.ai. It uses a YOLOv8 model to detect players from two different camera angles (broadcast and tacticam) and attempts to match them across views.

---

## 📁 Project Structure

![image](https://github.com/user-attachments/assets/e0a562b6-738c-411c-a949-c2860910dd25)

##Outputs:-
https://drive.google.com/drive/folders/1Wh_LD9UPSY3APWbK_J1RklPJAThk9hEv?usp=drive_link

## 🔧 Setup Instructions

### 1. Clone the repository
git clone https://github.com/Saraswat1/player-tracking.git
cd player-tracking
2. Set up a virtual environment (recommended)---
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install dependencies--
pip install -r requirements.txt
4. Download the YOLOv8 model
Place your trained best.pt model in the models/ directory (this is ignored in .gitignore).

You may use a pretrained YOLOv8 model if needed.


How to Run:-
python main.py

This will:-

Detect players from data/broadcast.mp4 and data/tacticam.mp4

Match players across the two videos

Save annotated outputs to the output/ folder as:-

broadcast_labeled.mp4

tacticam_labeled.mp4

Dependencies:-
Python 3.9+

Ultralytics YOLOv8

OpenCV

NumPy

Install all dependencies with: pip install -r requirements.txt
