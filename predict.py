import joblib

from flask import Flask, request, jsonify

encoder = joblib.load('./encoder.pkl')
final_model = joblib.load('./model.pkl')

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = final_model.predict([list(data.values())])
    return jsonify({"prediction": prediction[0]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
