print('Введите три числа')
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x + y > z:
    if y + z > x:
        if x + z > y:
            if x == y:
                if y == z:
                    print('Равносторонний треугольник')
                else:
                    print('Равнобедренный треугольник')
            elif x == z:
                print('Равнобедренный треугольник')
            elif z == y:
                print('Равнобедренный треугольник')
            else:
                print('Разносторонний треугольник')
        else:
            print('Не треугольник')
    else:
        print('Не треугольник')
else:
    print('Не треугольник')
