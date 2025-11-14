import array

def find_duplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return num

        num_set.add(num)

    return -1


arr = array.array('i', [10, 20, 13, 14, 15, 13, 17, 10, 20, 13])
print(find_duplicate(arr))