import re


word = str(input())
letters = re.split(r'\W', word)
letters_2 = list(letters[0])


for _i in range(len(letters_2)):
    check = letters_2.pop(0)
    if check in ['a', 'e', 'i', 'o', 'u'] and check.isalpha():
        print('vowel')
    elif check.isalpha():
        print('consonant')
