
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

# Load trained pipeline model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        input_data = [[
            (data['model']),
            int(data['year']),
            data['transmission'],    
            float(data['mileage']),
            data['fuelType'],
            float(data['tax']),
            float(data['mpg']),
            float(data['engineSize'])

        ]]
        prediction = model.predict(input_data)[0]
        return jsonify({'price': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
