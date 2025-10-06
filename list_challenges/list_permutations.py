import itertools as it

lst = ['A', 'B', 'C', 'D']

perms = it.permutations(lst, r=2)

perms_list = list(perms)

print('Permutations : ', perms_list)

for t in perms_list:
    print(t)
