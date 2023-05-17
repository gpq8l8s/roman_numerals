import argparse
import unittest

def fizz_buzz(number) :
    if number < 100:
        print("Number can't be bigger than 100!")
    elif number >= 100:
            if number % 3 == 0 and number % 5 == 0:
                return 'FizzBuzz'
            elif number % 3 == 0:
                return 'Fizz'
            elif number % 5 == 0:
                return 'Buzz'
            else :
                return number
            number += 1
            # all_numbers.append(number)

    if __name__ == '__main__':
        unittest.main()
        # parser = argparse.ArgumentParser()
        # args = parser.parse_args()
        # for number in range(args.integers[0]):
        #     print(fizz_buzz(number + 1))
        # print(number)