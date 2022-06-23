# 8)Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

x = 5   # столбцы
y = 4   # строки
a = []

for i in range(y):
    b = []
    s = 0
    print(f'The {i} row out of {y}')
    for j in range(x - 1):
        n = int(input('Enter a value: '))
        s += n
        b.append(n)
    b.append(s)
    a.append(b)
print(f'The 5x4 matrix with the last sum column:')
for i in a:
    print(i)

