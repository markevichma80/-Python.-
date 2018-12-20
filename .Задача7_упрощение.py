print('Введите три числа')
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x + y > z and y + z > x and x + z > y:
    if x == y or x == z or z == y:
        if x == y and y == z:
            print('Равносторонний треугольник')
        else:
            print('Равнобедренный треугольник')
    else:
        print('Разносторонний треугольник')
else:
    print('Не треугольник')
