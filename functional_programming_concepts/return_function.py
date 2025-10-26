def outer():
    def inner():
        print('Welcome')

    return inner

f = outer()
f()