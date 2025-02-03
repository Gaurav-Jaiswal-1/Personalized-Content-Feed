from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

# Load configuration variables
from app.utils.config import SECRET_KEY, DEBUG

# Initialize Flask app
app = Flask(__name__)

# Configure the Flask app
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DEBUG'] = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///data.db")
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "your-default-jwt-secret")

# Initialize JWT Manager
jwt = JWTManager(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Register authentication blueprint
from app.routes.auth_routes import auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix="/auth")

# Import models so they register with SQLAlchemy
from app.models.user import User
from app.models.content import Content

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# Optional: A simple route to test the app
@app.route("/")
def index():
    return "Welcome to the Personalized Content Feed API!"

if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000)
