def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def arithmetic(f,x,y):
    return f(x,y)

sum = arithmetic(add,10,5)
diff = arithmetic(sub,10,5)
print(sum,diff)