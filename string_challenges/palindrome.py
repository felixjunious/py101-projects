phrase = input('Enter a phrase : ')
text = phrase.casefold().replace(' ', '')
rev = text[::-1]

if text == rev:
    print(phrase)
else:
    print(text + rev)
