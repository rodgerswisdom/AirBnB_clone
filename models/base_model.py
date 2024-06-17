#!/usr/bin/python3

from datetime import datetime
import uuid

class BaseModel():
    """
    Class for all other 
    classes to inherit from
    """

    def __init__(self):
        self.id = uuid.uuid4
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def __str__(self):

        """Returns a string representation of the instance."""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute `updated_at` with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance's `__dict__`."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict