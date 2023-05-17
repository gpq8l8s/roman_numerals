import unittest
from src.fizz_buzz import fizz_buzz

class Testing(unittest.TestCase):
    def test_fizzbuzz(self):
            # Arrange
            
            # Act
            result = fizz_buzz(100)

            # Assert
            self.assertEqual(result, "Buzz")


if __name__ == '__main__':
    unittest.main()