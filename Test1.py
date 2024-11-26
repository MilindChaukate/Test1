import string


def reversestring(string):
    string = str(input("Please enter the string: "))
    return string[::-1]
print(reversestring(string))