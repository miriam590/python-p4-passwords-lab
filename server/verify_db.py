from app import app
from models import db, User

with app.app_context():
    print("Users table exists with records:", User.query.all())
