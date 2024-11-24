from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

# Flask app setup
app = Flask(__name__)
CORS(app)

# MongoDB Atlas setup
# Replace <username>, <password>, and <database> with your MongoDB Atlas details

try:
    client = MongoClient("mongodb+srv://victorphilemon001:Vixwebapp.2024@vix-web-app.0ukhw.mongodb.net/")
    db = client.vix_db
    db = client.test
    print("MongoDB connection successful!")
except Exception as e:
    print("Error connecting to MongoDB:", e)

services_collection = db.services
requests_collection = db.requests

# Routes
@app.route('/api/services', methods=['GET'])
def get_services():
    services = list(services_collection.find({}, {"_id": 0}))  # Exclude MongoDB ID
    return jsonify(services)

@app.route('/api/request-service', methods=['POST'])
def request_service():
    data = request.json
    requests_collection.insert_one(data)
    return jsonify({"message": "Service request submitted successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
