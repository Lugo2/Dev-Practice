
def array_diff(a, b):
    index = 0
    for element in a:
        if element == b[0]:
            a_removed = a.remove(element)
            b_removed = b.remove(element)
            str(a_removed)[1: -1]
            str(b_removed)[1: -1]
            c = str(a_removed)[1: -1] + str(b_removed)[1: -1]
            d = [c]
        index += 1
    return [d]

print(array_diff([1, 2], [1])) # == [2]

print(array_diff([1, 2, 2, 2, 3], [2])) # ==[1, 3]