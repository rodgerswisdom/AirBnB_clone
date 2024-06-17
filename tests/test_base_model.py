import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up the test case environment."""
        self.model = BaseModel()

    def test_id(self):
        """Test if id is a string and unique."""
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(len(self.model.id) > 0)

    def test_created_at(self):
        """Test if created_at is assigned correctly and is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is assigned correctly and is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method for the correct output format."""
        expected_output = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_output)

    def test_save(self):
        """Test if save method updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_to_dict(self):
        """Test if to_dict method returns a correct dictionary representation."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
