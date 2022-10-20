# 3,1415926535897932384626433832795

from Methods import enter
from Methods import calculate_pi as calc

accuracy = enter('Введите количество значащих цифр после запятой, которые нужно определить в числе пи: ')
pi = calc(accuracy)
print(f'Число пи с точностью до {accuracy}-го знака равно {pi}')