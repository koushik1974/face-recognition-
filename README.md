# 🧠 Real-Time Face Recognition with OpenCV & face_recognition

A real-time face recognition application built with **Python, OpenCV, and the `face_recognition` library**. The system detects and identifies known faces from a live webcam feed, highlights unknown faces, displays real-time FPS, and allows unknown faces to be saved and added to the recognition database dynamically.

---
## 📊 Dataset

The face recognition system uses a dataset of **210 face images across 30 individual celebrities** to build the known-face database.

* **300 total images - 210 train and 90 test**
* **30 unique identities**
* Multiple images per celebrity for identity representation
* **128-dimensional face encodings** used for identity matching

---
## 📸 Demo

The application performs real-time face detection and recognition through a webcam.

* 🟢 **Green label** — Recognized face
* 🔴 **Red label** — Unknown face
* 📊 Real-time **FPS monitoring**
* 🎥 Toggle between raw and processed webcam views

---

## 🚀 Features

* ✅ Real-time face detection and recognition
* ✅ Recognition of multiple faces simultaneously
* ✅ Pretrained **128-dimensional face encodings**
* ✅ FPS (Frames Per Second) monitoring
* ✅ Toggle between raw and processed webcam views
* ✅ Color-coded labels for known and unknown faces
* ✅ Save unknown faces and assign names dynamically
* ✅ Automatically incorporate newly saved faces into the recognition database
* ✅ Keyboard-controlled interface

---

## 🧠 How It Works

The system uses the `face_recognition` library to generate **128-dimensional face encodings** for known images and faces detected from the webcam.

During real-time inference:

1. The webcam captures a frame using **OpenCV**.
2. Faces are detected in the captured frame.
3. A 128-dimensional encoding is generated for each detected face.
4. The encoding is compared against the stored encodings of known identities.
5. The closest matching identity is displayed when a match is found.
6. Unknown faces are highlighted separately and can be saved for later identification.

No custom face-recognition model is trained in this project; it uses the pretrained functionality provided by the `face_recognition` library.

---

## 📁 Project Structure

```text
face-recognition-/
├── images/                 # Folder containing known face images
│   └── person_name.jpg
├── simple_facerec.py       # Face recognition class and matching logic
├── main.py                 # Main webcam application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV** — Webcam capture, image processing, and visualization
* **face_recognition** — Face detection and 128-dimensional face encodings
* **dlib** — Underlying face-recognition functionality

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/koushik1974/face-recognition-.git
cd face-recognition-
```

### 2. Install Dependencies

Make sure you have **Python 3.7–3.11** installed.

```bash
pip install -r requirements.txt
```

> ⚠️ The `dlib` dependency can be difficult to install on some systems. On Windows, you may need **CMake** and **Visual Studio Build Tools**.

### 3. Add Known Faces

Place clear, front-facing images of known people inside the `images/` directory.

The **filename is used as the person's label**.

Example:

```text
images/
├── person_name.jpg
├── friend_name.png
└── another_person.jpg
```

### 4. Run the Application

```bash
python main.py
```

The application will open your webcam and begin detecting and recognizing faces in real time.

---

## 🎮 Controls

| Key   | Action                                                        |
| ----- | ------------------------------------------------------------- |
| `ESC` | Exit the application                                          |
| `T`   | Toggle between raw and processed webcam views                 |
| `S`   | Save an unknown face and assign a name through terminal input |

---

## 🔄 Dynamic Unknown-Face Registration

When an unknown face is detected, press **`S`** to save the face.

The application allows you to:

1. Capture the unknown face.
2. Enter a name through the terminal.
3. Save the image to the known-face directory.
4. Use the newly added identity for subsequent recognition.

This makes it possible to expand the recognition database while the application is running.

---

## 📊 Performance Monitoring

The application displays the current **Frames Per Second (FPS)** directly on the webcam interface.

This provides a simple way to monitor real-time inference performance while processing live video.

---

## 📥 Download

You can clone the repository directly:

```bash
git clone https://github.com/koushik1974/face-recognition-.git
```

Or download the repository as a ZIP from GitHub.

---

## 🧑‍💻 Built With

* [OpenCV](https://opencv.org/)
* [dlib](http://dlib.net/)

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute the project according to the terms of the license.
