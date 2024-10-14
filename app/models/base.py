from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

# Initialize SQLAlchemy with no app bound
db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects in the system."""
    __abstract__ = True  # Ensures that class will not create its own table

    # Common columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def save(self):
        """
        Save a model instance
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete a model instance
        """
        db.session.delete(self)
        db.session.commit()