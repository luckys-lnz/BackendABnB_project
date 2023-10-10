#!/usr/bin/python3

""" Defines BaseModel class """
import uuid
from datetime import datetime

class BaseModel:
    """ Defines all the instances/attributes
        for other classes, and links to storage
    """

    def __init__(self):
        """ creating instances """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ returns string representation of the instances """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instace "updated_at" with current datetime """
        self.__dict__['updated_at'] = datetime.now()

    def to_dict(self):
        """ Returns keys/vals of __dict__ of the instance """
        res_dict = dict(self.__dict__)
        res_dict.update({
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        })
        return res_dict

