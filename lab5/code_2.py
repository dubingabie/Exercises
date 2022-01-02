
def does_have_digit(num,digit):
    for i in range(len(str(num))):
        if str(num)[i] == str(digit):
            return True
    return False


def fizz(num):
    if ( num % 3 == 0 ) or does_have_digit(num, 3):
        return True
    return False


def buzz(num):
    if ( num % 5 == 0 ) or does_have_digit(num, 5):
        return True
    return False


def fizzBuzz_2(num):
    return_value = ""
    if fizz(num):
        return_value += "Fizz"
    if buzz(num):
        return_value += "Buzz"
    if return_value == "":
        return_value = num
    return return_value

