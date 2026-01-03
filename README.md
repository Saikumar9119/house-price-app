✅ FINAL README.md (FULL, CLEAN, PRACTICAL)
# 🏠 House Price Prediction App

A complete end-to-end **machine learning project** that predicts house prices based on property features.
The project includes data preprocessing, model training, feature importance analysis, and a deployed Streamlit web app.

---

## 📌 What This Project Does

- Predicts house prices using a trained ML model
- Handles missing values and categorical data
- Explains which features affect house prices
- Provides a simple web interface using Streamlit

---

## 📂 Project Structure

```text
house-price-app/
├── app.py                        # Streamlit application
├── house_price_model.pkl         # Trained ML model (tracked with Git LFS)
├── requirements.txt              # Python dependencies
├── house_price_prediction.ipynb  # Model training notebook
└── README.md

🔹 Clone the Repository
git clone https://github.com/Saikumar9119/house-price-app.git
cd house-price-app

🔹 Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

🔹 Install Dependencies
pip install -r requirements.txt

🔹 Run the Streamlit App
streamlit run app.py


After running the command:

A browser window will open automatically

If not, open the URL shown in the terminal (usually http://localhost:8501)

🔹 How to Use the App

Enter house details:

Bathrooms

Size (BHK)

Total square feet

Location

Availability

Area type

Society

Balcony

Click Predict Price

The app displays the estimated house price

🤖 Model Information

Algorithm: RandomForestRegressor

Built using a full scikit-learn Pipeline

Preprocessing:

Numerical features: median imputation + scaling

Categorical features: most-frequent imputation + one-hot encoding

Evaluation Metric:

Mean Absolute Error (MAE)

🔍 Feature Importance

Feature importance was calculated using Permutation Importance.

Top features affecting house prices:

Number of bathrooms

Size (BHK)

Total square feet

Location

Availability

This helps explain why the model predicts a certain price.

🚀 Deployment Notes

The trained model is saved using joblib

Large model file is handled using Git LFS

The app is ready for deployment on Streamlit Cloud

🛠️ Technologies Used

Python

pandas, numpy

scikit-learn

Streamlit

Git & Git LFS
