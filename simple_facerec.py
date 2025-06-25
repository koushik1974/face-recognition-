import face_recognition
import cv2
import os
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.encoding_model = "hog"  # Use "cnn" if you have GPU and want better accuracy

    def load_encoding_images(self, images_path):
        """
        Load and encode all face images in the given folder.
        Filenames (without extension) will be used as labels.
        """
        print("[INFO] Loading images for encoding...")
        images_list = os.listdir(images_path)

        for img_name in images_list:
            if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(images_path, img_name)
                img = cv2.imread(img_path)

                if img is None:
                    print(f"[WARNING] Failed to load image: {img_name}")
                    continue

                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodings = face_recognition.face_encodings(rgb_img)

                if encodings:
                    self.known_face_encodings.append(encodings[0])
                    name = os.path.splitext(img_name)[0]
                    self.known_face_names.append(name)
                    print(f"[OK] Encoded {name}")
                else:
                    print(f"[WARNING] No face found in {img_name}")

        print(f"[INFO] Total known faces: {len(self.known_face_encodings)}")

    def detect_known_faces(self, frame):
        """
        Detect and identify known faces in the given frame.
        Returns a list of face locations and corresponding names.
        """
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame, model=self.encoding_model)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]

            face_names.append(name)

        # Scale face locations back to original frame size
        scaled_locations = [(top*4, right*4, bottom*4, left*4) for (top, right, bottom, left) in face_locations]
        return scaled_locations, face_names
