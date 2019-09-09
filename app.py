from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

#model = pickle.load(open('filename.pkl", 'rb'))

@app.route('/predict', methods=['POST'])
def predict_earnings():
    incoming_data = request.json
    prediction = model.predict(incoming_data)
    return jsonify(prediction)