s1 = input('Enter Phrase 1 : ')
s2 = input('Enter Phrase 2 : ')

s1 = s1.lower()
s2 = s2.lower()

for s in s1:
    if s.isalpha():
        if s1.count(s) == s2.count(s):
            print('Not Anagrams')
            break
else:
    print('Anagrams')