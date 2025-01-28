from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../.env")
    
    # Import and register blueprints
    from .routes.user_routes import user_blueprint
    from .routes.content_routes import content_blueprint
    
    app.register_blueprint(user_blueprint, url_prefix="/users")
    app.register_blueprint(content_blueprint, url_prefix="/content")
    
    return app
