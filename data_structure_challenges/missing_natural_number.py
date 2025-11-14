import array


def missing_number(arr):
    given_sum = 0
    actual_sum = 0

    for num in range(arr[0], arr[-1] + 1):
        given_sum += num

    for num in arr:
        actual_sum += num

    n = given_sum - actual_sum

    return n if n != 0 else None


arr1 = array.array('i',[1, 2, 3, 4, 5, 6, 7, 8, 10])
arr2 = array.array('i', [11, 12, 13, 15, 16, 17, 18])
arr3 = array.array('i', [1,2,3,4,5])

print(missing_number(arr1))
print(missing_number(arr2))
print(missing_number(arr3))