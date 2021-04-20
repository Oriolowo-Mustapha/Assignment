first_array = [2, 5, 6, 8]
second_array = [5, 4, 8, 9]
array = []
for element in first_array:
    if element in second_array:
        array.append(element)
        mul = array[-1] * array[-1]
        print(mul)