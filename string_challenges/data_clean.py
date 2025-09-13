scan = 'These+notes#reveal9Newton seeking-out an(!underlying structure to/the//pyramid'
clean = ''

for s in scan:
    if s.isalpha() or s.isspace():
        clean = clean + s
    else:
        clean = clean + ' '

print(clean)