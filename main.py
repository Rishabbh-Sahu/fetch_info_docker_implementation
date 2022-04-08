# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 2022
@author: Rishabbh sahu
"""
from flask import Flask, jsonify, request
from model import predict


# Create app
app = Flask(__name__)


# initialize the app
def initialize():
    """
    Start the app with the following message
    """
    print('<server is initialized>')


# Default landing page with caption
@app.route('/', methods=['GET'])
def hello():
    """
    Messages to be displayed in the landing page
    """
    response = {'Welcome': 'Hello from text pre-processing routine',}
    return jsonify(response)


@app.route('/fetch', methods=['POST'])
def fetch():
    input_json = request.json
    input_txt = input_json["text"]
    pre_processed_text = predict(input_txt)

    response = {
        "pre_processed_text": {
            "alphanumeric_text": pre_processed_text,
        },
        "algo": "Simple regex model",
    }
    return jsonify(response)


if __name__ == '__main__':
    initialize()
    # Run app
    app.run(host='0.0.0.0', port=5000, debug=False)
