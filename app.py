from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)
model = load_model("mnist_model.h5")

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            # 🧼 STEP 1: Load image
            img = Image.open(file).convert("L")      # Convert to grayscale
            img = img.resize((28, 28))               # Resize to 28x28

            # 🧼 STEP 2: Convert to array & reshape
            img_array = np.array(img)
            print("Before reshape:", img_array.shape, img_array.dtype)

            img_array = img_array.reshape(1, 784)    # Flatten for Dense model
            img_array = img_array.astype("float32") / 255.0  # Normalize

            print("After reshape:", img_array.shape, img_array.dtype)

            # 🧠 STEP 3: Predict
            prediction = model.predict(img_array)
            predicted_digit = np.argmax(prediction)
            confidence = np.max(prediction) * 100
            prediction = f"{predicted_digit} (Confidence: {confidence:.2f}%)"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
