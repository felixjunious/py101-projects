l = [10,20,30,40,50]

try:
    try:
        index = int(input('Enter Index'))
    except ValueError as e:
        print(e)

    print(l[index])
except IndexError as e:
    print(e)
except Exception as e:
    print(e)