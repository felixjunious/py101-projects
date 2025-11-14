import array

def max_product(arr):
    x = None
    y = None
    max_prod = None

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            prod = arr[i] * arr[j]
            if max_prod is None or prod > max_prod:
                x = arr[i]
                y = arr[j]
                max_prod = prod

    return x, y

arr1 = array.array("i",[2, 4, 6, 8, 3, 7, 9])
arr2 = array.array("i", [0, -1, -3, -5, -8, 2, 4])

print(max_product(arr1))
print(max_product(arr2))