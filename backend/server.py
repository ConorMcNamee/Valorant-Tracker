from flask import Flask
from flask_cors import CORS, cross_origin
from flask.json import jsonify
import requests
import json

import env as env

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'

@app.route('/', methods=['GET'])
def index():
    return("Welcome!")

@app.route('/val-data', methods=['GET'])
@cross_origin()
def getValorantData():
    val_data = requests.get("https://ap.api.riotgames.com/val/content/v1/contents?api_key=RGAPI-e056a228-a10e-481c-8338-9469355fc27c")
    return jsonify(val_data.json())

@app.route('/acc-data', methods=['GET'])
@cross_origin()
def getAccountData():
    acc_data = requests.get("https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"+env.val_username+"/"+env.val_tagline+"?api_key="+env.API_KEY)
    return jsonify(acc_data.json())

def getMatchData():
    pass


if __name__ == '__main__':
    app.run(debug=True)