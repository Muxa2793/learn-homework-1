"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее

*Доработайте ask_user() так, чтобы когда пользователь вводил 
  вопрос который есть в словаре, программа давала ему 
  соответствующий ответ. Например: 
  Пользователь: Что делаешь?
  Программа: Программирую
"""


def ask_user():
  
  ask_question = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую'
  }
  
  while True:
      user_say = input('Программа: Как дела?\nПользователь: ')
      if user_say.lower() == 'хорошо':
        print('Программа: Это отлично! Спроси меня что-нибудь. Например: "Как дела?" или "Что делаешь?"\nЧто бы закончить - напиши "пока"')
        while True:
          user_say = input('Пользователь: ')
          if user_say.lower() == 'как дела?':
            print(f"Программа: {ask_question['Как дела?']}\nПрограмма: Спроси ещё что нибудь")
          elif user_say.lower() == 'что делаешь?':
            print(f"Программа: {ask_question['Что делаешь?']}\nПрограмма: Спроси ещё что нибудь")
          elif user_say.lower() == 'пока':
            print('Программа: Надеюсь ещё увидимся!')
            break
      user_say == 'пока'
      print('Программа: Пока!')
      break
          

def main():
  ask_user()

if __name__ == "__main__":
  main()
