lst = input("Введите числа через пробел:").split()
print(lst)
for i in range(len(lst)):
    lst[i] = int(lst[i])

print(lst)
elements = []
elem_sum = 0
for i in range(len(lst)):
    if i % 2 != 0:
        elements.append(lst[i])
        elem_sum += lst[i]

for i in range(len(elements)):
    elements[i] = str(elements[i])

print(f'На нечетных позициях элементы: {" и ".join(elements)}, ответ: {elem_sum}')
