import unittest
from src.svg_updater import update_svg
import os

class TestSvgUpdate(unittest.TestCase):
    def test_update_svg(self):

        # Arrange
        file_path = os.path.join(os.getcwd(), "test\data\\test.svg")
        print(file_path)
        new_name = "test"
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        new_file_path = os.path.join(downloads_path, f"{new_name}_new.svg")

        # Act
        update_svg(file_path, new_name)

        # Assert
        self.assertTrue(os.path.exists(new_file_path))

        # Cleanup
        os.remove(new_file_path)

if __name__ == "__main__":
    unittest.main()