
# 🧠 MNIST Handwritten Digit Recognition Web App

A simple machine learning and web application project that uses a neural network trained on the MNIST dataset to recognize handwritten digits (0–9). The project features a Python-based backend using **Keras** for model training and **Flask** for deployment.

---

## 📁 Project Structure

```
mnist-project/
│
├── MNIST.ipynb         # Jupyter notebook for training the model
├── mnist_model.h5      # Pretrained Keras model (Dense Neural Network)
├── app.py              # Flask web server to host the digit recognition interface
├── templates/
│   └── index.html      # HTML template for file upload and result display
├── requirements.txt    # List of Python dependencies
└── README.md           # Project description and setup instructions
```

---

## 🚀 Features

- Trains a simple feedforward neural network on the MNIST dataset.
- Saves the model (`.h5`) for reuse in web applications.
- Users can upload an image of a digit and receive predictions via the Flask interface.
- Includes a confidence score with each prediction.

---

## 🧪 Model Summary

- **Architecture:** 2 Dense layers with ReLU activation and Dropout
- **Input:** 784-dimensional vector (flattened 28x28 grayscale image)
- **Output:** 10 classes (digits 0 through 9)
- **Accuracy:** ~97% on test set

---

## 🖥️ How to Run the Project

### 🔧 Prerequisites

Install the required libraries:

```bash
pip install -r requirements.txt
```

Ensure you have:
- Python 3.7+
- TensorFlow / Keras
- Flask
- Pillow

### 🧠 Train the Model

Open `MNIST.ipynb` and run all cells to train the model. It will generate a file called `mnist_model.h5`.

> **Tip:** Skip this step if `mnist_model.h5` is already included.

### 🌐 Run the Web App

```bash
python app.py
```

This will start a local web server (typically at `http://127.0.0.1:5000/`).

---

## 📷 Usage

1. Open the app in your browser.
2. Upload an image of a handwritten digit (ideally 28x28 or a clear black-on-white digit).
3. Get the predicted digit and confidence score.

---

## 📊 Example Output

```
Predicted Digit: 4
Confidence: 98.27%
```

---

## ✅ To-Do

- Add image preprocessing to handle larger image sizes and inversion
- Improve UI using CSS or Bootstrap
- Deploy on Heroku or Render

---

## 📚 Dataset

This project uses the [MNIST dataset](http://yann.lecun.com/exdb/mnist/), which consists of 60,000 training and 10,000 test grayscale images of handwritten digits.

---

## 👨‍💻 Author

**GitHub:** [@priyarv13](https://github.com/priyarv13)
