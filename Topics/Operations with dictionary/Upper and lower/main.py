# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
a = dict(zip(dict.fromkeys(some_iterable), some_iterable))
b = dict((k.upper(), v.lower()) for k, v in a.items())
print(b)
