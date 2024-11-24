from flask import Flask
from flask_cors import CORS
from routes.main import main_blueprint
from routes.auth import auth_blueprint

app = Flask(__name__)
CORS(app)  # Allow React to communicate with Flask

# Register blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
