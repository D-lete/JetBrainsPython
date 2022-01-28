text = input()
words = text.split()
for word in words:
    if word.lower().startswith(('www.', 'https://', 'http://')):
        word.join('\n')
        print(word)
