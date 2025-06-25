import cv2
import time
import os
from simple_facerec import SimpleFacerec

sfr = SimpleFacerec()
sfr.load_encoding_images("images")

cap = cv2.VideoCapture(0)

# FPS calculation
frame_count = 0
start_time = time.time()

# Mode toggle
show_processed = True
unknown_count = 0

while True:
    ret, frame = cap.read()
    raw_frame = frame.copy()

    if show_processed:
        face_locations, face_names = sfr.detect_known_faces(frame)

        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

            # Text size
            (text_width, text_height), _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_DUPLEX, 1, 2)

            # Draw name background
            cv2.rectangle(frame, (x1, y1 - text_height - 10), (x1 + text_width, y1), color, cv2.FILLED)
            cv2.putText(frame, name, (x1, y1 - 5), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

            # Draw face rectangle
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    # FPS calculation
    frame_count += 1
    if frame_count >= 10:
        end_time = time.time()
        fps = frame_count / (end_time - start_time)
        start_time = end_time
        frame_count = 0

    if 'fps' in locals():
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    # Instructions overlay
    cv2.putText(frame, "Press ESC to exit | S to save unknown | T to toggle view", (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

    # Show frame
    cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1)

    if key == 27:  # ESC to exit
        break

    elif key == ord('t') or key == ord('T'):
        show_processed = not show_processed

    elif key == ord('s') or key == ord('S'):
        # Save unknown face
        face_locations, face_names = sfr.detect_known_faces(raw_frame)

        for face_loc, name in zip(face_locations, face_names):
            if name == "Unknown":
                y1, x2, y2, x1 = face_loc
                face_img = raw_frame[y1:y2, x1:x2]
                cv2.imshow("Unknown Face", face_img)
                cv2.waitKey(1)

                user_name = input("Enter name for this face: ").strip()
                if user_name:
                    save_path = f"images/{user_name}_{unknown_count}.jpg"
                    cv2.imwrite(save_path, face_img)
                    print(f"Saved new face to {save_path}")
                    sfr.load_encoding_images("images")  # Reload encodings
                    unknown_count += 1

cv2.destroyAllWindows()
cap.release()
