# 🩺 Breast Cancer Classifier

---

## 🚀 Project Overview

This project is a **machine learning web application** that predicts whether a tumor is **Malignant (Cancer)** or **Benign (No Cancer)** based on 30 features from the **Wisconsin Breast Cancer Dataset (WDBC)**.

- Built using **Python, Flask, and scikit-learn**
- Provides both a **web form** for browser input and a **JSON API** for Postman
- Model trained using **Random Forest Classifier** for high accuracy

---

## 📊 Dataset

- **Name:** Wisconsin Diagnostic Breast Cancer (WDBC) Dataset  
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))  
- **Size:** 569 samples, 32 columns  
- **Target Column:** `diagnosis` (M → Malignant, B → Benign)  
- **Features:** 30 numeric features (mean, standard error, worst) of cell nuclei

**Example Features:**  
`radius_mean`, `texture_mean`, `perimeter_mean`, `area_mean`, `smoothness_mean`, …

---

## 🧰 Project Structure

```
Breast_Cancer_Classifier/
│
├── data/                         # Dataset files
│ └── wdbc.csv
│
├── models/                       # Saved trained model
│ └── model.pkl
│
├── app.py                        # Flask web application
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Installation




1. **Create virtual environment and activate**
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

2. **Install dependencies**

bash
pip install -r requirements.txt


3. **Run the Flask app locally**
bash
python app.py


- Open browser: http://127.0.0.1:5000/

- Postman JSON API: http://127.0.0.1:5000/predict
```
## 🖥️ Usage
### Browser

- Enter 30 comma-separated numeric feature values in the text box

- Click Predict → result displayed instantly

## 📈 Model Performance

### Algorithm: Random Forest Classifier

### Accuracy: 97.9%

## Classification Report
```Class	Precision	Recall	F1-score
Benign (B)	0.98	0.99	0.98
Malignant (M)	0.97	0.95	0.96
Avg/Total	0.98	0.98	0.98

```
## 🛠️ Technologies Used

- Python 3.x
- Flask
- scikit-learn
- pandas & numpy
- HTML/CSS
```
```
## RENDER LINK: 
https://breast-cancer-classifier-2e6t.onrender.com

