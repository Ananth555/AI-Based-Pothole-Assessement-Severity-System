# AI-Based-Pothole-Assessement-Severity-System
# 🚧 AI-Based Pothole Detection & Authority Assessment System

## 📌 Project Overview

This project is an AI-powered system designed to automatically detect potholes on roads using computer vision and deep learning. It helps municipal authorities identify road damage and take timely action.

The system uses object detection models to analyze road images and highlight potholes with bounding boxes.

---

## 🎯 Objectives

* Detect potholes from road images
* Improve road safety by early identification
* Assist municipal authorities with data-driven decisions
* Automate manual inspection process

---

## 🧠 Technologies Used

* Python 🐍
* YOLOv8 (Ultralytics)
* Roboflow (Dataset & Annotation)
* OpenCV
* NumPy
* Matplotlib

---

## 📂 Dataset Details

* Total Images: 1000+
* Train: 745 images
* Validation: 199 images
* Test: 100 images

### 🔄 Data Augmentation

* Grayscale
* Blur & Motion Blur
* Noise
* Exposure adjustment
* Horizontal Flip

---

## ⚙️ Model Training

* Model: YOLOv8 Object Detection
* Framework: Ultralytics
* Training on custom pothole dataset
* Optimized for real-time detection

---

## 📸 Output Results

* Detects potholes with bounding boxes
* Provides confidence scores
* Works on images and video frames

---

## 🚀 Features

* Real-time pothole detection
* High accuracy using deep learning
* Easy integration with dashboards
* Scalable for smart city applications

---

## 🖥️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/pothole-detection.git

# Navigate to project folder
cd pothole-detection

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
# Run detection
python detect.py
```

---

## 📊 Future Improvements

* Live camera integration
* Mobile app for reporting potholes
* Severity classification (small, medium, large)
* GPS-based mapping system

---

## ⭐ Acknowledgements

* Roboflow for dataset tools
* Ultralytics for YOLOv8 model
* Open-source community

---

## 📌 Conclusion

This project demonstrates how AI can be used to solve real-world infrastructure problems by automating pothole detection and improving road maintenance efficiency.
