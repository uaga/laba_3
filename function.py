def fibonacci(n):
    array = []
    for i in range(n):
        if i == 0: array.append(1)
        if i == 1: array.append(1)
        if i > 1: array.append(array[i - 1] + array[i - 2])
    return array


def sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def calc(a, b, operator):
    return {
        operator == "+": a + b,
        operator == "-": a - b,
        operator == "/": a / b,
        operator == "*": a * b
    }[True]

