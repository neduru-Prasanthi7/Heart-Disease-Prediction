from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

# Load model and scaler
with open("Heart_data.pkl", "rb") as f:
    model = pickle.load(f)

with open("scalar.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def fun():
    return render_template('index.html')

@app.route("/predict",methods = ['GET','POST'])
def fun3():
    a = [float(i) for i in request.form.values()]
    b = [np.array(a)]
    b = scaler.transform(b)
    predictions = model.predict(b)
    predictions = predictions[0]
    if predictions == 0:
        return render_template('index.html',prediction_text = "No Heart Disease Detected")
    else:
        return render_template('index.html', prediction_text="Heart Disease Detected")

if __name__ == "__main__":
    app.run(debug=True)