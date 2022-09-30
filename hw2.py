lst = input("Введите числа через пробел:").split()
print(lst)
for i in range(len(lst)):
    lst[i] = int(lst[i])

print(lst)

new_lst = []
for i in range(len(lst)):
    while len(lst) > 1:
        new_lst.append(lst.pop() * lst.pop(0))
if len(lst) == 1:
    new_lst.append(lst[0] ** 2)

print(new_lst)
