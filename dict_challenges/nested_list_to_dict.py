header = ['name', 'age', 'city']
data = [
    ['James', 25, 'NY'],
    ['Kiran', 30, 'DEL'],
    ['Smith', 24, 'PAR'],
    ['Raj', 27, 'DEL']
]

res = {}

for i, head in enumerate(header):
    curr_head = {}
    for row in data:
        key = row[i]
        curr_head.setdefault(key,[]).append(row)
    res[head] = curr_head

print("Dictionaries:")
for i in range(len(header)):
    print('\n' + header[i])
    for key, value in res[header[i]].items():
        print(f"{key:<10}: {value}")
