import datetime
import string


def challenge1(first_name, last_name):
    return "%s %s" % (last_name, first_name)


print(challenge1("John", "Doe"))


def challenge2(num):
    if num % 2 == 0:
        return "This number is even"
    else:
        return "This number is odd"


print(challenge2(99999990))


def challenge3(b, h):
    return 1/2 * b * h


print(challenge3(4, 2))


def challenge4(numb):
    if numb == 0:
        return "This is zero"
    elif numb < 0:
        return "This number is negative"
    else:
        return "This number is positive"


print(challenge4(6))


def challenge5(r):
    return 3.14 * r ** 2


print(challenge5(5))


def challenge6(r):
    return 4/3 * 3.14 * r ** 3


print(challenge6(4))


def challenge7(n):
    return n * n + n


print(challenge7(9))


def challenge8(integer):
    if integer in range(150, 3000):
        return "This number is between 150 and 3000"
    else:
        return "This number is not between 150 and 3000"


print(challenge8(500))
vowels = ['a', 'e', 'i', 'o', 'u']


def challenge9(letter):
    if letter in vowels:
        return "This is a vowel"
    else:
        return "This is a constant"


print(challenge9("r"))

number = ['5', '7', '8', '6']
length = 0


def challenge10():
    for i in range(len(number)):
        if number[i] == string.ascii_letters:
            return "This string is not numeric"
        else:
            return "This string is not numeric"


print(challenge10())

datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

print(datetime.datetime.now())


def challenge12(a, b):
    while b != 0:
        gcd = b
        b = a % b
        a = gcd
    print("The denominator is %d" % a)


print(challenge12(3, 4))
