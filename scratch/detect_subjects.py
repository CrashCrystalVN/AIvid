import cv2
import json
from pathlib import Path

audit_dir = Path(r"C:\Users\vuasu\.gemini\antigravity\scratch\AIvid\scratch\flow_frame_audit")
face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
upperbody_cascade_path = cv2.data.haarcascades + 'haarcascade_upperbody.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
upperbody_cascade = cv2.CascadeClassifier(upperbody_cascade_path)

detections = {}

for img_path in sorted(audit_dir.glob("*.jpg")):
    if img_path.parent.name == "annotated":
        continue
    img = cv2.imread(str(img_path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    upperbodies = upperbody_cascade.detectMultiScale(gray, 1.1, 3)
    
    face_list = [{"x": int(x), "y": int(y), "w": int(w), "h": int(h), "x2": int(x+w)} for (x, y, w, h) in faces]
    body_list = [{"x": int(x), "y": int(y), "w": int(w), "h": int(h), "x2": int(x+w)} for (x, y, w, h) in upperbodies]
    
    detections[img_path.name] = {
        "faces": face_list,
        "upperbodies": body_list
    }

print(json.dumps(detections, indent=2))
