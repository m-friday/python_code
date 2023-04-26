# num = "12321, 55555, 45554, 11611"
# print(num[::-1])


def isPalindrome(number):
    input = number
    firtDigit = input % 10
    print(firtDigit)
    input = int(input / 10)
    print(input)
    secondDigit = input % 10
    input = int(input / 10)
    thirdDigit = input % 10
    input = int(input / 10)
    fourthdiDigit= input % 10
    input = int(input / 10)
    print(input)
    fifthDigit = input % 10
    result = (firtDigit * 10000) + (secondDigit * 1000) + (thirdDigit * 100) + (fourthdiDigit * 10) + fifthDigit
    print(result)
    if number == result:
        return True
    else:
        return False


print(isPalindrome(12221))
