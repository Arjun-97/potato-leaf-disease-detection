from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "potato_leaf.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Define class labels
CLASS_NAMES = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]

def preprocess_image(image_file):
    """Convert uploaded image into a format compatible with the model."""
    image = Image.open(image_file)
    image = image.resize((128, 128), Image.BILINEAR)
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["GET", "POST"])
def detect():
    prediction = None
    if request.method == "POST":
        if "file" not in request.files or request.files["file"].filename == "":
            return render_template("detect.html", prediction="No file uploaded.")

        file = request.files["file"]
        try:
            processed_image = preprocess_image(file)
            predictions = model.predict(processed_image)
            predicted_class = CLASS_NAMES[np.argmax(predictions)]
            return render_template("detect.html", prediction=predicted_class)
        except Exception as e:
            return render_template("detect.html", prediction=f"Error processing image: {str(e)}")

    return render_template("detect.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

