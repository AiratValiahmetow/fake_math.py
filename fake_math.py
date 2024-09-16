def divide(first, second):


    if second == 0:
        return 'Ошибка'
    else:
        result = first / second
    return result
result1 = divide(69, 3)
result2 = divide(3, 0)
print(result1)
print(result2)