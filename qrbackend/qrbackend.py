import json
import os
from flask import Flask, request, jsonify, url_for
from .qr import get_qr_code

app = Flask(__name__)

@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    r = request.get_json()    
    qr = get_qr_code(r['string'])
    qr.save(os.path.dirname(os.path.abspath(__file__)) + '/static/qr.png') 
    url_qr = 'http://localhost:5000' +  url_for('static', filename='qr.png')
    resp = {"url": url_qr }
    return jsonify(resp)
