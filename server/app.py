from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-SQLAlchemy
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
