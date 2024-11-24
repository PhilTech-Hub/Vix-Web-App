from flask import Blueprint, jsonify
from services.database import get_database

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/api/services", methods=["GET"])
def get_services():
    db = get_database()
    services = db.services.find()  # Assuming a `services` collection
    result = [{"id": str(s["_id"]), "name": s["name"], "description": s["description"]} for s in services]
    return jsonify(result)
