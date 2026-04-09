import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image
import pandas as pd
import cv2
import tempfile

# Page config
st.set_page_config(page_title="Pothole Detection System", layout="wide")

# Sidebar
st.sidebar.title("⚙️ Settings")
confidence = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)

st.title("🚧 AI-Based Pothole Detection System")
st.markdown("Upload an image or video to detect potholes and classify them by size.")

# Load model
model = YOLO("best.pt")

uploaded_file = st.file_uploader("Upload Image or Video", type=["jpg", "png", "jpeg", "mp4"])

if uploaded_file is not None:

    # IMAGE PROCESSING
    if uploaded_file.type.startswith("image"):

        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)

        img = np.array(image)

        results = model.predict(img, conf=confidence)

        result_img = results[0].plot()

        with col2:
            st.subheader("Detected Image")
            st.image(result_img, use_column_width=True)

        boxes = results[0].boxes.xyxy.cpu().numpy()
        scores = results[0].boxes.conf.cpu().numpy()

        data = []

        for box, score in zip(boxes, scores):
            x1, y1, x2, y2 = box
            area = (x2 - x1) * (y2 - y1)

            if area < 5000:
                size = "Small"
            elif area < 15000:
                size = "Medium"
            else:
                size = "Large"

            data.append([
                "Pothole",
                round(float(score), 2),
                int(area),
                size
            ])

        df = pd.DataFrame(data, columns=["Detection", "Confidence", "Area", "Size"])

        st.subheader("📊 Detection Summary")
        st.write(f"Total Potholes Detected: **{len(df)}**")

        st.dataframe(df, use_container_width=True)

        # Download CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Report (CSV)",
            data=csv,
            file_name="pothole_report.csv",
            mime="text/csv",
        )

        # Download detected image
        result_pil = Image.fromarray(result_img)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        result_pil.save(temp_file.name)

        with open(temp_file.name, "rb") as file:
            st.download_button(
                label="📥 Download Detected Image",
                data=file,
                file_name="detected_output.jpg",
                mime="image/jpeg",
            )

    # VIDEO PROCESSING (Basic Support)
    elif uploaded_file.type.startswith("video"):

        st.subheader("Uploaded Video")
        st.video(uploaded_file)

        st.info("⚡ For full video detection, frame-by-frame processing can be added.")