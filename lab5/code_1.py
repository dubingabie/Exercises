

def fizzBuzz_1(num):
    return_value = ""
    if num % 3 == 0:
        return_value += "Fizz"
    if num % 5 == 0:
        return_value += "Buzz"
    if return_value == "":
        return_value = num
    return return_value
