from __future__ import print_function
from flask import Flask, request, jsonify
import json
import pprint
import requests
import sys
import urllib
import os
import json
import psycopg2

app = Flask(__name__)

class Business():

    def __init__(self):
        pass

@app.route('/api/business', methods=['GET'])
def get_businesses():
    pass

@app.route('/api/business/<id>', methods=['GET'])
def get_business(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)