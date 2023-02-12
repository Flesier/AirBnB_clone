#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """basemodel class"""
    def __init__(self, *args, **kwargs):
        """initializes class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """returns string function"""
        return self.__str__()

    def save(self):
        """saves the class"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """gives a dict of object"""
        copy = dict(self.__dict__)
        copy['__class__'] = str(self.__class__.__name__)
        copy['created_at'] = self.created_at.isoformat()
        copy['updated_at'] = self.updated_at.isoformat()
        return copy
