lists = [[1,2,3], [1,1,1,1,1], [2,2,3,3]]

res = []

for lst in lists:
    if len(lst) > len(res):
        res = lst.copy()

print('Longest list :', res)