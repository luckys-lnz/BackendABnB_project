#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime



class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if isinstance(value, str):
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models.__init__ import storage
            storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update the public instance attribute updated_at."""
        from models import storage  # Import here to avoid circular import
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_result = self.__dict__.copy()
        dict_result['__class__'] = self.__class__.__name__
        dict_result['created_at'] = self.created_at.isoformat()
        dict_result['updated_at'] = self.updated_at.isoformat()
        return dict_result

