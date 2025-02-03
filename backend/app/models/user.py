from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    # Dummy authentication method for demonstration.
    @staticmethod
    def authenticate(username, password):
        # Replace this with real password verification
        user = User.query.filter_by(username=username).first()
        if user and user.password_hash == password:  # Replace with secure hash check
            return user
        return None

    def serialize(self):
        return {
            "user_id": self.user_id,
            "username": self.username
        }
