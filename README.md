# 🏠 House Price Prediction App

An end-to-end machine learning application that predicts house prices based on property features.  
The project covers data preprocessing, model training, feature importance analysis, and deployment using Streamlit.

---

## 📌 Project Overview

- Predicts house prices using a trained ML model
- Handles missing values and categorical data correctly
- Identifies key features influencing house prices
- Provides a simple and interactive web interface

---

## 📂 Project Structure

```text
house-price-app/
├── app.py                        # Streamlit application
├── house_price_model.pkl         # Trained model (managed with Git LFS)
├── requirements.txt              # Python dependencies
├── house_price_prediction.ipynb  # Model training notebook
└── README.md
````

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Saikumar9119/house-price-app.git
cd house-price-app
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
# venv\Scripts\activate       # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧑‍💻 How to Use the App

1. Enter house details:

   * Bathrooms
   * Size (BHK)
   * Total square feet
   * Location
   * Availability
   * Area type
   * Society
   * Balcony
2. Click **Predict Price**
3. View the estimated house price

---

## 🤖 Model Information

* Algorithm: **RandomForestRegressor**
* Implemented using a full **scikit-learn Pipeline**
* Preprocessing:

  * Numerical features: median imputation + scaling
  * Categorical features: most-frequent imputation + one-hot encoding
* Evaluation Metric:

  * **Mean Absolute Error (MAE)**

---

## 🔍 Feature Importance

Feature importance is calculated using **Permutation Importance**.

Top features affecting house prices:

* Number of bathrooms
* Size (BHK)
* Total square feet
* Location
* Availability

This helps explain why the model predicts a particular price.

---

## 🌐 Deployment Notes

* Model is saved using `joblib`
* Large model file is handled using **Git LFS**
* Application is ready for deployment on **Streamlit Cloud**

---

## 🛠️ Tech Stack

* Python
* pandas, numpy
* scikit-learn
* Streamlit
* Git & Git LFS

---

## 👤 Author

**Sai Kumar**
Aspiring Data Scientist

````

---

### What to do after pasting
```bash
git add README.md
git commit -m "Add final clean README"
git push
````

That’s it.
