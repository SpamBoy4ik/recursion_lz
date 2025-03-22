def find_gcd(number1, number2):
    if number1 == 0 or number2 == 0:
        return (number1+number2)
    if number1 > number2:
        number1 = number1 % number2
    else:
        number2 = number2 % number1
    return find_gcd(number1, number2)


def main():
    print('Нахождение НОД двух чисел.')
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите Второе число: '))
    print(f'НОД({number1}, {number2}) = {find_gcd(number1, number2)}')


if __name__ == '__main__':
    main()    
