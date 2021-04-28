def palindrome():
    word = str(input())
    if word == word[::-1]:
        print('Palindrome')
    else:
        print('Not palindrome')


palindrome()
