def convert_to_base(number, base):
    convert_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    if number < 0:
        return  '-' + str(convert_to_base(abs(number), base))
    if number < base:
        return convert_digits[number]
    return str(convert_to_base(number // base, base)) + str(convert_digits[number % base])


def main():
    print('Перевод числа в другую систему счисления (от 2 до 16).')
    number = int(input('Введите число: '))
    base = int(input('Введите систему счисления для перевода (от 2 до 16): '))
    print(convert_to_base(number, base))


if __name__ == '__main__':
    main()
