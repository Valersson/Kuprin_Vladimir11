# функция чтобы найти сумму цифр числа
def sum_of_digits(num):
    numbers = 0
    while num != 0:
        last_digit = num % 10
        numbers += last_digit
        num = num // 10
    return numbers
# создание списка
cube_list = []
for number in range(1, 1001):
    if number % 2 != 0:
        cube_list.append(number ** 3 + 17)
# вычисление суммы тех чисел из этого списка,
# сумма цифр которых делится на 7
sum_of_some_numbers_from_list = 0
for i in cube_list:
    if sum_of_digits(i) % 7 == 0:
        sum_of_some_numbers_from_list =+ sum_of_digits(i)
print(sum_of_some_numbers_from_list)