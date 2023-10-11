import pickle

from flask import Flask, request, jsonify


with open('dv.bin', 'rb') as file:
    dv = pickle.load(file)

with open('model.bin', 'rb') as file:
    model = pickle.load(file)

app = Flask('credit_score')


@app.route('/score', methods=['POST'])
def score():
    client = request.get_json()

    ytest = dv.transform([client])
    y_pred = model.predict_proba(ytest)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'credit_score': float(y_pred.round(3)),
        'credit': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9090)
