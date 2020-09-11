"""
Домашнее задание №1
Цикл while: ask_user
* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def ask_user():

  while True:
    user_say = input('Программа: Как дела?\nПользователь: ')
    user_say = user_say.lower()
    if user_say == 'хорошо':
      print('Программа: Отлично. Надеюсь ещё увидимся!')
      break
          
def main():
  ask_user()

if __name__ == "__main__":
  main()
