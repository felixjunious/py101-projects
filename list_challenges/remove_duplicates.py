l1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]

res = []

for x in l1:
    if x not in res:
        res.append(x)

print(res)