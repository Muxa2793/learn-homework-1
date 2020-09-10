"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
  
  ASK_QUESTION = {
    'как дела': 'Хорошо',
    'что делаешь': 'Программирую'
  }
  
  while True:
    try:
      user_say = input('Программа: Как дела?\nПользователь: ')
      user_say = user_say.lower()
      if user_say == 'хорошо':     
        print(
          'Программа: Это отлично! Спроси меня что-нибудь.',
          'Например: "Как дела?" или "Что делаешь?"',
          '\nЧтобы закончить нажми "Ctrl+с".'
        )
        while True:
          user_say = input('Пользователь: ')
          user_say = user_say.lower()
          if 'как дела' in user_say:
            print(f"Программа: {ASK_QUESTION['как дела']}\nПрограмма: Спроси ещё что-нибудь")
          elif 'что делаешь' in user_say:
            print(f"Программа: {ASK_QUESTION['что делаешь']}\nПрограмма: Спроси ещё что-нибудь")
    except KeyboardInterrupt:
      print('\nПока!')
      break
  
    
if __name__ == "__main__":
    ask_user()
