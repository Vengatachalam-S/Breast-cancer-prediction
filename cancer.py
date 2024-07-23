from flask import Flask, render_template, request
from sklearn.ensemble import IsolationForest  # Assuming the model is pre-trained and saved

app = Flask(__name__)

# Load the pre-trained model (replace with your actual loading logic)
model = IsolationForest()  # Assuming the model is already trained and saved

@app.route("/")
def index():
    return render_template("index.html")  # Render the HTML template

@app.route("/predict", methods=["POST"])
def predict():
    # Get user input from the form
    heart_rate = request.form.get("heart_rate")
    blood_pressure = request.form.get("blood_pressure")

    # Preprocess and reshape data for prediction (replace with your logic)
    data = [[float(heart_rate), float(blood_pressure)]]

    # Make prediction
    prediction = model.predict(data)[0]

    # Prepare data for the template
    result = {
        "heart_rate": heart_rate,
        "blood_pressure": blood_pressure,
        "anomaly": "Anomaly" if prediction == -1 else "Normal",
    }

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
