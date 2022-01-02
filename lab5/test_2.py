
from code_2 import *

def test_fizzBuzz_2():
    assert fizzBuzz_2(3) == "Fizz"
    assert fizzBuzz_2(123) == "Fizz"
    assert fizzBuzz_2(132) == "Fizz"
    assert fizzBuzz_2(322) == "Fizz"
    assert fizzBuzz_2(123) == "Fizz"
    assert fizzBuzz_2(5) == "Buzz"
    assert fizzBuzz_2(511) == "Buzz"
    assert fizzBuzz_2(125) == "Buzz"
    assert fizzBuzz_2(551) == "Buzz"
    assert fizzBuzz_2(175) == "Buzz"
    assert fizzBuzz_2(165) == "FizzBuzz"
    assert fizzBuzz_2(15) == "FizzBuzz"
    assert fizzBuzz_2(101) == 101
    assert fizzBuzz_2(404) == 404
    assert fizzBuzz_2(727) == 727
