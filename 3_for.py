"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():

  school_class_scores = [
      {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
      {'school_class': '4b', 'scores': [2, 5, 2, 3, 4]}
  ]

  scores_sum_avg = 0
  for scores in school_class_scores:
    scores_sum_avg += sum(scores['scores'])/len(scores['scores'])

  print(f'Средний балл по всей школе: {round(scores_sum_avg/len(school_class_scores),1)}')

  print('\nСредний балл по классам:')
  for average_score in school_class_scores:
    school_class = average_score['school_class']
    school_class_avg = sum(average_score['scores'])/len(average_score['scores'])
    print(f'Средний балл {school_class} класса: {school_class_avg}')

if __name__ == "__main__":
    main()
