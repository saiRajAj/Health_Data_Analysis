# 🏥 Health Data Analysis and Disease Prediction

## 📌 Project Overview
This project is a **Python-based Health Data Analysis system** that analyzes patient medical and lifestyle data to predict the risk of disease. It follows the complete **data science and machine learning lifecycle**, from data preprocessing to prediction.

The system allows users to **enter new patient details at runtime**, processes the data, and predicts whether the patient is at risk using a **Logistic Regression** model.

-----

## 🎯 Objectives
- Analyze health and lifestyle data
- Identify important factors influencing disease
- Visualize health data patterns
- Predict disease risk using Machine Learning
- Provide user-based disease prediction

---

## 📊 Dataset Description
The dataset contains the following attributes:

| Column | Description |
|------|------------|
| Age | Age of the patient |
| Gender | Male / Female |
| BMI | Body Mass Index |
| BloodPressure | Blood pressure level |
| Glucose | Glucose level |
| Cholesterol | Cholesterol level |
| Smoking | Smoking habit (Yes/No) |
| PhysicalActivity | Low / Medium / High |
| Disease | Target variable (1 = Disease, 0 = No Disease) |

---

## 🛠 Technologies Used
- Python 3
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn

---

## 📂 Project Structure
```
health_project/
│
├── dataset.csv
├── preprocessing.py
├── analysis.py
├── visualization.py
├── model.py
├── predict.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How the Project Works
1. **Data Preprocessing**  
   - Encodes categorical variables into numerical form
   - Generates a cleaned dataset

2. **Exploratory Data Analysis (EDA)**  
   - Statistical summary of data
   - Disease distribution analysis

3. **Data Visualization**  
   - Age distribution histogram
   - BMI vs Disease box plot
   - Correlation heatmap

4. **Model Training**  
   - Logistic Regression model
   - Model trained on cleaned dataset
   - Accuracy and classification report generated

5. **User-Based Prediction**  
   - User enters new patient details
   - System predicts disease risk

---

## ▶️ How to Run the Project

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run files in order
```bash
python preprocessing.py
python analysis.py
python visualization.py
python model.py
python predict.py
```

---

## 🔮 Prediction Logic
The Logistic Regression model calculates a probability score.  
- If probability ≥ 0.5 → **Disease Detected**  
- If probability < 0.5 → **No Disease**

---

## 📈 Sample Output
```
Disease Probability: 0.88
⚠️ Disease Risk Detected
```

---

## 🎓 Academic Use
- Mini Project
- Data Science Lab
- Machine Learning Lab
- Portfolio Project

---

## 🚀 Future Enhancements
- Web application using Flask or Streamlit
- Larger real-world dataset
- Multiple disease prediction
- Cloud deployment

---

## 👨‍💻 Author
**Sairaj Garud**

---

## 📄 License
This project is for **educational purposes only**.

