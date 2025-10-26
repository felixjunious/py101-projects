# Example 1
k = lambda x: x * 2

print(k(3))

# Example 2
a = lambda x,y: x + y

print(a(5,10))

# Example 3
print((lambda x: x + 2)(5))

# Example 4
l1 = [1,2,3,4,5,6,7,8,9,10]
f = filter(lambda x: x % 3 == 0, l1)
l2 = list(f)
print(l2)

# Example 5
l3 = [1,2,3,4]
l4 = list(map(lambda x: -x, l3))
print(l4)

# Example 6
l5 = [1,2,3,4,5,6,7,8,9,10]
k = lambda x: x if x%2==0 else -x
l6 = list(map(k,l5))
print(l6)

# Example 7
l7 = [[4,2,'Six'],[1,4,'Five'],[2,2,'Four']]
l8 = sorted(l7, key=lambda x: x[0]+x[1])
print(l8)

