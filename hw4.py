n = int(input("Введите преобразуемое число: "))
binary_list = []
while n != 1:
    binary_list.append(n % 2)
    n = n // 2
else:
    binary_list.append(1)
binary_list = binary_list[::-1]

for i in range(len(binary_list)):
    binary_list[i] = str(binary_list[i])

print(''.join(binary_list))
