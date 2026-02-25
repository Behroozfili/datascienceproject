from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd 
from src.datascienece.pipeline.prediction_pipline import PredictionPipline 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict_route():
    if request.method == 'POST':
        try:
            # 1. Collect input data with exact feature names
            # Proline is excluded as it is the TARGET_COLUMN
            data = [
                int(request.form.get('class', 0)),
                float(request.form.get('Alcohol', 0)),
                float(request.form.get('Malic_acid', 0)),
                float(request.form.get('Ash', 0)),
                float(request.form.get('Alcalinity_of_ash', 0)),
                int(request.form.get('Magnesium', 0)),
                float(request.form.get('Total_phenols', 0)),
                float(request.form.get('Flavanoids', 0)),
                float(request.form.get('Nonflavanoid_phenols', 0)),
                float(request.form.get('Proanthocyanins', 0)),
                float(request.form.get('Color_intensity', 0)),
                float(request.form.get('Hue', 0)),
                float(request.form.get('OD280_OD315', 0))
            ]

            # 2. Reshape into an array with 13 features
            data_array = np.array(data).reshape(1, 13)
            
            # 3. Initialize and run the prediction pipeline
            pipeline = PredictionPipline()
            pred = pipeline.predict(data_array)
            
            # 4. Format the result (rounded to 2 decimal places)
            result = round(float(pred[0]), 2)
            return render_template('result.html', prediction=str(result))

        except Exception as e:
            print(f"DEBUG - Error details: {e}")
            return render_template('index.html', prediction=f"Calculation Error: {str(e)}")

    return render_template('index.html', prediction=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)