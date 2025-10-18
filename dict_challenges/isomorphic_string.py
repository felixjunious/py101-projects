str1 = input('Enter the first string : ')
str2 = input('Enter the second string')

is_isomorphic = True

if len(str1) != len(str2):
    is_isomorphic = False
else:
    z = zip(str1,str2)
    map1, map2 = {}, {}

    for char1,char2 in z:
        if char1 not in map1.keys():
            map1[char1] = char2
        else:
            if map1[char1] != char2:
                is_isomorphic = False

        if char2 not in map2.keys():
            map2[char2] = char1
        else:
            if map2[char2] != char1:
                is_isomorphic = False

if is_isomorphic:
    print(f'{str1} & {str2} are isomorphic')
else:
    print(f'{str1} & {str2} are not isomorphic')
