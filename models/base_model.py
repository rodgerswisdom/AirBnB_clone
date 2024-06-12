#!/usr/bin/python3

from datetime import datetime
import uuid

class BaseModel():
    """
    Class for all other 
    classes to inherit from
    """

    def __init__(self, *args, **kwargs):
        self.id = uuid.uuid4
        self.updated_at = datetime.now()
        self.created_at = datetime.now()