import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
models = pickle.load(open('models.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = models.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='Anomaly Prediction (0: Benign; 1: Infiltered):  {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = models.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)