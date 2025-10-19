def flatten(lst):
    for item in lst:
        if hasattr(item, '__iter__'):
            yield from flatten(item)
        else:
            yield item

if __name__ == '__main__':

    test_list = [1,2,[3,4,[5,6,7],8],9,[10,11]]

    flat = flatten(test_list)
    flat_list = list(flat)

    print(flat_list)