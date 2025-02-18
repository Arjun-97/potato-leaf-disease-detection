# Potato Leaf Disease Detection

## Overview
Potato plants are susceptible to various diseases that can significantly impact crop yield. This project provides a **Potato Leaf Disease Detection** system using **Deep Learning** to classify leaves as:
- **Early Blight**
- **Late Blight**
- **Healthy**

The model is built using **TensorFlow** and is deployed using **Flask**, allowing users to upload an image of a potato leaf and get an instant diagnosis.

## Features
✅ AI-based detection of potato leaf diseases
✅ User-friendly web interface
✅ Instant classification of uploaded images
✅ Helps farmers and researchers take preventive measures

## Requirements
- **Python 3.12 or below** (TensorFlow does not support Python 3.13 yet)
- **Flask** for backend
- **TensorFlow** for model inference
- **Pillow** for image processing
- **NumPy** for numerical operations

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Arjun-97/potato-leaf-disease-detection.git
   cd potato-leaf-disease-detection
   ```
2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. **Start the Flask Server**
   ```bash
   python app.py
   ```
2. **Open in Your Browser**
   Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. **Upload an Image**
   - Navigate to the detector page
   - Upload an image of a potato leaf
   - Get instant predictions!

## Folder Structure
```
/your-project-folder
│── app.py                # Flask application
│── potato_leaf.keras     # Trained deep learning model
│── requirements.txt      # Dependencies list
│── templates/            # HTML templates
│   ├── about.html        # About us page
│   ├── index.html        # Landing page
│   ├── detect.html       # Detection page
│── static/               # CSS, JS
│   ├── style.css         # CSS classes for the project
```

## Future Improvements
🎨 Improve UI with a better frontend framework (e.g., Vue.js, React)

