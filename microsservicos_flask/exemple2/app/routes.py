# app/routes.py

from flask import current_app as app
from flask import jsonify

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")
