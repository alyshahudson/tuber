from tuber import app, config
from flask import send_from_directory, send_file, request, Response
import requests
import os

@app.route('/')
def home():
    if config.flask_env != "production":
        return requests.get(f'http://localhost:8081/').content
    return send_file(os.path.join(config.static_path, "index.html"))

@app.route('/<path:path>')
def files(path):
    if config.flask_env != "production":
        headers = {}
        for header in ["Accept"]:
            if header in request.headers:
                headers[header] = request.headers[header]
        req = requests.get(f'http://localhost:8081/{path}', headers=headers)
        resp = Response(req.content)
        for i in req.headers.keys():
            resp.headers[i] = req.headers[i]
        return resp
    return send_from_directory(config.static_path, path)

@app.errorhandler(404)
def default(e):
    return send_file(os.path.join(config.static_path, "index.html"))
