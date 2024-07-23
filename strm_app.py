import streamlit as st
from sklearn.ensemble import IsolationForest  # Assuming the model is pre-trained and saved

# Load the pre-trained model (replace with your actual loading logic)
model = IsolationForest()  # Assuming the model is already trained and saved

def predict(heart_rate, blood_pressure):
  """
  Function to make predictions using the loaded model.

  Args:
      heart_rate: User input for heart rate.
      blood_pressure: User input for blood pressure.

  Returns:
      str: "Anomaly" if predicted as anomalous, "Normal" otherwise.
  """
  data = [[float(heart_rate), float(blood_pressure)]]
  prediction = model.predict(data)[0]
  return "Anomaly" if prediction == -1 else "Normal"

# Title and header
st.title("Health Monitoring Prediction")
st.header("Enter patient data")

# Input fields for user data
heart_rate = st.number_input("Heart Rate", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)

# Button to trigger prediction
if st.button("Predict"):
  # Make prediction and display results
  prediction = predict(heart_rate, blood_pressure)
  st.write(f"**Heart Rate:** {heart_rate}")
  st.write(f"**Blood Pressure:** {blood_pressure}")
  st.write(f"**Predicted Anomaly:** {prediction}")

