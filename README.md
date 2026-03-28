#  Customer Segmentation & Prediction System

##  Project Overview
This project builds an end-to-end Machine Learning pipeline to segment customers based on purchasing behavior and predict customer segments using supervised learning.

The system transforms raw transactional data into meaningful insights using **RFM (Recency, Frequency, Monetary) analysis**, clustering, and classification models.



##  Objectives
- Segment customers into meaningful groups
- Understand customer behavior patterns
- Predict customer segments for new data
- Build a deployable ML application



## Dataset
- Transactional retail dataset (customer purchases)
- Contains:
  - CustomerID
  - InvoiceNo
  - InvoiceDate
  - Quantity
  - UnitPrice
  - Description
  - Country

---

## Workflow

### 1. Data Preprocessing
- Removed duplicate rows (~0.9%)
- Handled missing values (~3.1%)
- Dropped rows with missing `CustomerID`
- Converted data types (CustomerID → int, InvoiceDate → datetime)

---

### 2. Feature Engineering (RFM Analysis)
Created customer-level features:
- **Recency** → Days since last purchase
- **Frequency** → Number of unique purchases
- **Monetary** → Total spending

---

### 3. Unsupervised Learning (Clustering)
- Algorithm: **K-Means**
- Optimal clusters selected using:
  - Elbow Method
  - Silhouette Score
- Final clusters: **3**

#### Customer Segments:
-  High Value Customers  
- Regular Customers  
- Churned Customers  

---

### 4. Supervised Learning (Prediction)
Trained models to predict customer segments:
- Random Forest Classifier  
- XGBoost Classifier  

Techniques used:
- Train-test split  
- Cross-validation  
- Hyperparameter tuning (GridSearchCV)

---

### 5. Model Evaluation
- Classification Report (Precision, Recall, F1-score)
- Feature Importance Analysis

---

### 6. Deployment
- Built a web application using **Streamlit**
- Users can input:
  - Recency
  - Frequency
  - Monetary  
- App predicts customer segment in real-time

---

##  Key Learnings
- Importance of data cleaning and preprocessing
- Feature engineering is critical for model performance
- Understanding data structure (transaction vs customer level)
- Combining unsupervised and supervised learning
- Building end-to-end ML pipelines
- Deploying ML models using Streamlit

---

##  Project Structure
customer-segmentation-ml/
│
├── app/
│ └── app.py
│
├── models/
│ └── customer_segment_model.pkl
│
├── notebooks/
│ └── (EDA & development notebooks)
│
├── requirements.txt
└── README.md

Streamlit link: https://trnrdja4appy7emqy2twyre.streamlit.app/
