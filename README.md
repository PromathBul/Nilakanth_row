# Задача
Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

# Решение
В решении использовалс ряд Нилоканта.

Ряд Нилоканта выглядит следующим образом:

$4 + \frac{4}{4 * 3 * 2} - \frac{4}{6 * 5 * 4} + \frac{4}{8 * 7 * 6} - \frac{4}{10 * 9 * 8} + ...$

Число пи определяется как сумма элементов, расчитанная в цикле. Знак слагаемого опеределяется по кратности четырем первого числа в знаменателе. Если число кратно 4, то знак положительный, иначе - отрицательный. С кажлым циклом значение первого числа знаменателя увеличивается на 2.

Окончание цикла происходит тогда, когда значение слагаемого по модулю меньше, чем установленная точность. Например, если точность установлена до 2 значащих цифр после запятой, то величина последнего слагаемого должна быть меньше 0,01 ($10^{-2}$).