for number in range(1, 101):
    print(number, end=' ')
    if number % 10 == 1:
        print('процент')
    elif 2 <= number%10 <= 4:
        print('процента')
    else:
        print('процентов')