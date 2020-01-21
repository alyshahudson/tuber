from tuber import app, config, db
from flask import send_from_directory, send_file, request, jsonify
from tuber.models import *
from tuber.permissions import *
import datetime
import uuid

@app.route("/api/shifts/list")
def list_shifts():
    shifts = db.session.query(Shift).all()
    return jsonify({"success": True, "strings": shifts})


@app.route("/api/shfits", methods=["POST"])
def create_shift():
    print(request.json)
