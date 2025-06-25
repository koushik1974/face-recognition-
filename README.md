
# 🧠 Real-Time Face Recognition with OpenCV & face_recognition

A powerful and simple real-time face recognition app using Python, OpenCV, and the `face_recognition` library.

---

## 📸 Demo

*Live webcam face recognition, labeling known faces and highlighting unknown ones.*

---

## 🚀 Features

- ✅ Detect and recognize faces in real-time
- ✅ FPS (Frames per second) display
- ✅ Toggle between raw and processed views (`T` key)
- ✅ Save unknown faces and assign names dynamically (`S` key)
- ✅ Color-coded labels (green = known, red = unknown)
- ✅ Bold instructions overlay (`ESC` to exit)

---

## 📁 Folder Structure

```
face-recognition-app/
├── images/                 # Folder with known face images
│   └── your_name.jpg
├── simple_facerec.py       # Face recognition class
├── main.py                 # Main webcam application
├── requirements.txt        # Python dependencies
└── README.md               # You're reading this!
```

---

## 🛠️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/face-recognition-app.git
cd face-recognition-app
```

2. **Install dependencies:**

Make sure you have Python 3.7–3.11 installed.

```bash
pip install -r requirements.txt
```

> ⚠️ `dlib` can be tricky to install on some systems. On Windows, you may need CMake and Visual Studio Build Tools. See [dlib install help](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/).

3. **Add known face images:**

Place clear, front-facing images into the `images/` folder. The filename will be used as the label.

Example:
```
images/
├── ElonMusk.jpg
├── YourFriend.png
```

4. **Run the app:**

```bash
python main.py
```

---

## 💡 Controls

- `ESC` – Exit
- `T` – Toggle processed/raw webcam frame
- `S` – Save unknown face and assign a name via terminal input

---

## 📥 Download ZIP

If you don't use Git, you can also [**Download ZIP**](https://github.com/your-username/face-recognition-app/archive/refs/heads/main.zip) and extract it manually.

---

## 🧑‍💻 Credits

Built using:
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [dlib](http://dlib.net/)

---

## 📜 License

This project is licensed under the MIT License – feel free to use and modify it for your projects!

---

> Made with ❤️ by Bathula Koushik Yadav
