import joblib
import streamlit as st
import numpy as np

# Load trained model
model = model = joblib.load('models/customer_segment_model.pkl')

# Page config
st.set_page_config(page_title="Customer Segmentation App")

st.title("🛍️ Customer Segmentation Predictor")
st.write("Enter customer behavior to predict segment")

st.sidebar.header("Input Features")

# Input fields
recency = st.number_input("Recency (days since last purchase)", min_value=0, value=50)
frequency = st.number_input("Frequency (number of purchases)", min_value=1, value=2)
monetary = st.number_input("Monetary (total spend)", min_value=0.0, value=500.0)

# Prediction button
if st.button("Predict Segment"):

    input_data = np.array([[recency, frequency, monetary]])

    prediction = model.predict(input_data)[0]

    # Map cluster to segment
    segment_map = {
        0: "Regular Customer",
        1: "Churned Customer",
        2: "High Value Customer"
    }

    segment = segment_map.get(prediction, "Unknown")

    # Display result
    st.success(f"Predicted Segment: {segment}")

    # Optional interpretation
    if segment == "High Value Customer":
        st.write("💎 This customer is highly valuable. Focus on retention.")
    elif segment == "Regular Customer":
        st.write("📦 This customer is consistent. Opportunity to upsell.")
    else:
        st.write("⚠️ This customer may churn. Consider re-engagement strategies.")