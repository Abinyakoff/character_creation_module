from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для '
           'вычисления квадратного корня из заданного числа')
message_2 = ('Мы вычислили квадратный корень '
             'из введённого вами числа. Это будет:')


def calc(your_number: float):
    """Проверка, что число меньше 0."""
    if your_number >= 0:
        all_number = calculate_square_root(your_number)
        return print(message_2, all_number)
    return None


def calculate_square_root(number: float):
    """Вычисляет квадратный корень."""
    return sqrt(number)


print(message)
calc(25.5)
