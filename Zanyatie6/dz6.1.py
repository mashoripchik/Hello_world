# Дан список. Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке. Все слова: посчитать количество гласных и согласных. Вывести всё на экран.
n = [15, 48, 'hello', 6, 19, 'world']
n1 = (n[0:2] + n[3:5])
n2 = n[2::3]
print(n1)
print(n2)
a = [int(n1) for n1 in n1]
print(a)
sum = 0
for i in a:
    if i % 2 == 0:
        sum += i
    print(sum)
else:
