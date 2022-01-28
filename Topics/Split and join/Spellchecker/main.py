dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
checked_ok = []
for word in sentence:
    if word not in dictionary:
        word.join('\n')
        print(word)
    elif word in dictionary:
        checked_ok.append(word)
        if len(checked_ok) == len(sentence):
            print('OK')
