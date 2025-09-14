from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Metadata object for table info
metadata = MetaData()

# SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# Define Pet model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
