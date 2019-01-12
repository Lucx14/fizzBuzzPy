import pytest

from fizzBuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
