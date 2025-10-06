word_set = {'plea', 'medical', 'listen', 'leap', 'decimal', 'silent', 'pale', 'enlist'}

res = set()

for word1 in word_set:
    for word2 in word_set:
        if word1 != word2 and sorted(word1) == sorted(word2):
            res.add(tuple(sorted((word1,word2))))

for pair in res:
    print(pair)
