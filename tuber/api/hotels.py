from tuber import app, config, db
from flask import send_from_directory, send_file, request, jsonify
from tuber.models import *
from tuber.permissions import *
import requests

headers = {
    'X-Auth-Token': config['uber_api_token']
}

@app.route("/api/hotel/staffer_auth", methods=["POST"])
def staffer_auth():
    req = {
        "method": "attendee.search",
        "params": [
            request.json['token'],
            "full"
        ]
    }
    resp = requests.post(config['uber_api_url'], headers=headers, json=req)
    id = resp.json()['result'][0]['id']
    success = id == request.json['token']
    return jsonify({"success": success})