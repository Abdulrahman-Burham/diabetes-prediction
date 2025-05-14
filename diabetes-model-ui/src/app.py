from flask import Flask, render_template, request
import pandas as pd
from model import predict_diabetes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('h.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'age': request.form['age'],
            'gender': request.form['gender'],
            'bmi': request.form['bmi'],
            'glucose': request.form['glucose'],
            'insulin': request.form['insulin'],
            'bp': request.form['bp'],
            'pedigree': request.form['pedigree'],
            'activity': request.form['activity'],
            'smoker': request.form['smoker'],
            'family': request.form['family'],
            'hba1c': request.form['hba1c']
        }
        
        # Call the prediction function
        prediction = predict_diabetes(data)
        
        return render_template('h.html', prediction=prediction)
    except Exception as e:
        return render_template('h.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)