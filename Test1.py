from itertools import count


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count = count + 1
    return count
string = str(input("Enter the string: "))
print(count_vowels(string))
