import unittest
from src.to_roman import num_to_roman

class Testing(unittest.TestCase):
    def test_roman(self):
            # Arrange
            
            # Act
            result = num_to_roman(4)

            # Assert
            self.assertEqual(result, "IV")


if __name__ == '__main__':
    unittest.main()