def challenge1(firstname, lastname):
    return "%s %s" % (lastname, firstname)


print(challenge1("John", "Doe"))


def challenge2(number):
    if number % 2 == 0:
        return "This number is even"
    else:
        return "This number is odd"


print(challenge2(99999990))


def challenge3(b, h):
    return 1/2 * b * h


print(challenge3(4, 2))


def challenge4(number):
    if number == 0:
        return "This is zero"


def challenge5(r):
    return 3.14 * r ** 2


print(challenge5(5))


def challenge6(r):
    return 4/3 * 3.14 * r ** 3


print(challenge6(4))


vowels = ['a', 'e', 'i', 'o', 'u']


def challenge9(letter):
    if letter in vowels:
        return "This is a vowel"
    else:
        return "This is a constant"


print(challenge9("r"))
