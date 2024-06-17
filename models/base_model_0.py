from datetime import datetime

class BaseModel:
    def __init__(self):
        self.updated_at = datetime.now()
    
    def save(self):
        """Updates the public instance attribute `updated_at` with the current datetime."""
        self.updated_at = datetime.now()
