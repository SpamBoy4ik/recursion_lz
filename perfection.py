def is_perfect_number(number, divider = 2, sum = 1):
    if sum == number:
        return True
    if sum > number:
        return False
    if number % divider == 0:
        sum += divider
    return is_perfect_number(number, divider + 1, sum)


print('Проверка числа на совершенность.')
number = int(input('Введите число: '))
if is_perfect_number(number):
    print('Число совершенное.')
else:
    print('Число несовершенное.')