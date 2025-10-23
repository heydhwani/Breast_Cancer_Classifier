# app.py
from flask import Flask, request, render_template_string, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the saved model
model = joblib.load('models/model.pkl')

# Your existing HTML template
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Breast Cancer Predictor</title>
</head>
<body style="font-family:Arial; text-align:center; margin-top:40px;">
    <h2>🩺 Breast Cancer Prediction</h2>
    <p>Enter 30 feature values (comma separated):</p>
    <form method="post">
        <textarea name="features" rows="4" cols="70" placeholder="e.g. 17.99,10.38,122.8,1001,0.1184,..."></textarea><br><br>
        <input type="submit" value="Predict" style="padding:10px 20px;">
    </form>
    {% if result %}
        <h3>Prediction: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

# 1️⃣ Root route for HTML form (browser)
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            # Get input values from HTML form
            features = [float(x.strip()) for x in request.form['features'].split(',')]
            arr = np.array(features).reshape(1, -1)
            prediction = model.predict(arr)[0]
            result = "Malignant (Cancer)" if prediction == 1 else "Benign (No Cancer)"
        except:
            result = "⚠️ Invalid Input! Please enter 30 numeric values."
    return render_template_string(HTML, result=result)

# 2️⃣ /predict route for Postman JSON requests
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [float(x.strip()) for x in data['features'].split(',')]
        arr = np.array(features).reshape(1, -1)
        prediction = model.predict(arr)[0]
        result = "Malignant (Cancer)" if prediction == 1 else "Benign (No Cancer)"
    except:
        result = "⚠️ Invalid Input! Please enter 30 numeric values."
    return jsonify({"prediction": result})

# 3️⃣ Run Flask using Render dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT or default 5000
    app.run(host="0.0.0.0", port=port)
