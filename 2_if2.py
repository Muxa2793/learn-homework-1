"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты   

"""

def comparing_strings(str_1, str_2):
  if type(str_1) != str or type(str_2) != str:
    return 0
  if str_1 == str_2:
    return 1
  if str_1 != str_2 and len(str_1) > len(str_2) and 'learn' != str_2:
    return 2
  if str_1 != str_2 and 'learn' in str_2:
    return 3


def main():
  print(comparing_strings(42, 'Это строка'))
  print(comparing_strings('Это строка ', 'Это строка '))
  print(comparing_strings('Эта строка длинее', 'Этой строки'))
  print(comparing_strings('Python', 'learn'))
    

if __name__ == "__main__":
    main()
