from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
import pickle
from tensorflow import keras
from keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

app = Flask(__name__)
CORS(app)

# Load the pre-trained LSTM model and tokenizer

model = keras.models.load_model('sentiment_model.h5')
with open('/home/nrj-srj/Music/Full stack project final year/flask-server/model main/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

@app.route("/members")
def members():
    return {"members": ["Member1","Member2","Member3"]}

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']

    # Preprocess the text
    sequence = tokenizer.texts_to_sequences([text])
    sequence = pad_sequences(sequence, maxlen=100)

    # Make predictions
    prediction = model.predict(sequence)[0]

    # Convert prediction to human-readable format
    if np.any(prediction > 0.5):
        output = 'Positive'
        print("positive")
    else:
        output = 'Negative'
        print("negative")

    # Return the response as JSON
    return jsonify({'prediction': output})

if __name__ == "__main__":
    app.run(debug=True)