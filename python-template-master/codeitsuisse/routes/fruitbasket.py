import logging
import json
from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def getdummy():
    geo = request.get_json()
    result = 287
    return result