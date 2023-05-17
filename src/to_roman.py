import unittest
import roman

def num_to_roman(number):
    to_roman = roman.toRoman(number)
    return to_roman
    # num=[1, 4, 5, 9, 10, 40, 50, 90,
    #     100, 400, 500, 900, 1000]
    # roman= ["I", "IV", "V", "IX", "X", "XL",
    #     "L", "XC", "C", "CD", "D", "CM", "M"]
    

if __name__ == '__main__':
    unittest.main()