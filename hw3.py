lst = input("Введите вещественные числа через пробел:").split()
print(lst)
for i in range(len(lst)):
    lst[i] = float(lst[i])

new_lst = []

for i in range(len(lst)):
    if lst[i] % 1 != 0:
        new_lst.append(round(lst[i] % 1, 2))

print(new_lst)
print(max(new_lst) - min(new_lst))
