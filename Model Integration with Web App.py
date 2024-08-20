from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

# Dummy model for demonstration
model = RandomForestClassifier()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)