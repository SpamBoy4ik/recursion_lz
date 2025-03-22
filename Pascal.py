def pascal_triangle(level, triangle = [[1]]):
    if len(triangle) == level:
        return triangle
    row = [1] + triangle[len(triangle) - 1]
    for i in range(1, len(row) - 1):
        row[i] += row[i + 1]
    triangle.append(row)
    return pascal_triangle(level, triangle)


def list_print(list):
    for i in list:
        print(i, sep = '\n')


def main():
    print('Построение треугольника Паскаля n уровня.')
    level = int(input('Введите n: '))
    list_print(pascal_triangle(level))


if __name__ == '__main__':
    main()    
