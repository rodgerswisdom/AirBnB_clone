import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
import json

class TestHBNBCommand(unittest.TestCase):
    """Unittests for the HBNBCommand class."""

    def setUp(self):
        """Set up test environment."""
        self.console = HBNBCommand()
        self.storage_file = "file.json"
        try:
            with open(self.storage_file, 'r') as file:
                self.backup = json.load(file)
        except FileNotFoundError:
            self.backup = {}

    def tearDown(self):
        """Tear down test environment."""
        # Restore storage state
        with open(self.storage_file, 'w') as file:
            json.dump(self.backup, file)

    def test_create_missing_class_name(self):
        """Test create command with no class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create command with a valid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)
            self.assertIn("BaseModel", storage.all())

    def test_show_missing_class_name(self):
        """Test show command with no class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show InvalidClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with no instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_no_instance_found(self):
        """Test show command with a valid class name but non-existent id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_valid_instance(self):
        """Test show command with a valid class name and id."""
        base_model = BaseModel()
        base_model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {base_model.id}")
            self.assertIn(base_model.id, f.getvalue().strip())

    def test_destroy_missing_class_name(self):
        """Test destroy command with no class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClass 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with no instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_no_instance_found(self):
        """Test destroy command with a valid class name but non-existent id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_valid_instance(self):
        """Test destroy command with a valid class name and id."""
        base_model = BaseModel()
        base_model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {base_model.id}")
            self.assertNotIn(base_model.id, storage.all())

    def test_all_invalid_class(self):
        """Test all command with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_valid_class(self):
        """Test all command with a valid class name."""
        base_model = BaseModel()
        base_model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_all_all_instances(self):
        """Test all command with no class name."""
        base_model = BaseModel()
        base_model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_update_missing_class_name(self):
        """Test update command with no class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update InvalidClass 1234 attr value")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with no instance id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_missing_attribute(self):
        """Test update command with no attribute name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with no attribute value."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234 attr")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_valid_instance(self):
        """Test update command with a valid class name and id."""
        base_model = BaseModel()
        base_model.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {base_model.id} name 'NewName'")
            self.assertEqual(base_model.name, 'NewName')

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

if __name__ == "__main__":
    unittest.main()
