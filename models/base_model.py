#!/usr/bin/python3

# from datetime import datetime
# import uuid

# class BaseModel():
#     """
#     Class for all other 
#     classes to inherit from
#     """

#     def __init__(self):
#         self.id = uuid.uuid4
#         self.updated_at = datetime.now()
#         self.created_at = datetime.now()

#     def __str__(self):

#         """Returns a string representation of the instance."""

#         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

#     def save(self):
#         """Updates the public instance attribute `updated_at` with the current datetime."""
#         self.updated_at = datetime.now()

#     def to_dict(self):
#         """Returns a dictionary containing all keys/values of the instance's `__dict__`."""
#         obj_dict = self.__dict__.copy()
#         obj_dict['__class__'] = self.__class__.__name__
#         obj_dict['created_at'] = self.created_at.isoformat()
#         obj_dict['updated_at'] = self.updated_at.isoformat()
#         return obj_dict

"""This file contain the parent class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        __init__ constructor method of the class
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__ method that returns string representation of the instance
        Returns:
        [str]: instance of BaseModel string representation"""
        st = "[{:s}] ({:s}) {}"
        return st.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        save method that saves instance information in JSON file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict method that return dictionary representation of the instance

        Returns:
            [dict]: dictionary with information about the BaseModel instance
        """
        new = dict(self.__dict__)
        new["__class__"] = type(self).__name__
        new["created_at"] = new["created_at"].isoformat()
        new["updated_at"] = new["updated_at"].isoformat()

        return new
