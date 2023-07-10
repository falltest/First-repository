from dataclasses import dataclass

questions = [
    {'text': "Сколько было найдено планет "
             "за пределами Солнечной системы?",
     'answers': ["< 1k", "1k - 10k", "10k - 1kk", "> 1kk",],
     'rigth_answer_index': 1,
     'explanation' : None    
    }


@dataclass
class Question:
    text: str
    answers: list[str]
    rigth_answer_index: int
    explanation: str | None = None
    rigth_answers_indexes: list[int] | None = None

    {'text': "Сколько лет Cолнцу?",
     'answers': ["< 1k", "1k - 10k", "10k - 1kk", "> 1kk",],
     'rigth_answer_index': 3,
     'explanation' : None    
    }
]

for question in questions:
    print(question['text'])
    print(*question['answers'],sep='\n')
    answer_from_user = input()
    rigth_answer_index = question['rigth_answer_index']
    if answer_from_user != question['answers'][rigth_answer_index]:
        print(f"Неправильно! Правильный ответ {question['answers'][rigth_answer_index]}")
    @property
    def rigth_answer(self):
        return self.answers[self.rigth_answer_index]

questions = [
    Question(text = "Сколько было найдено планет за пределами Солнечной системы?",
            answers=["< 1k", "1k - 10k", "10k - 1kk", "> 1kk",],
            rigth_answer_index=1,
            explanation='Планеты искать сложно'),
    Question(text = "Сколько лет Земле?",
            answers=["2023", "8000", "6.5ккк", "Земли не существует"],
            rigth_answer_index=1),
    Question(text = "Солнце является ...",
            answers=["Белым карликом", "Желтым карликом", "Солнца не сущесвует", "Красным гигантом"],
            rigth_answer_index=1),

]


def main():
    from time import sleep

question = {
    'text' : 'текст вопроса',
    'answers': ['а', 'б', 'в'],
    'right_answer_index' : 0,
    'explanation' : 'объяснение'
 }
    for question in questions:
        print(question.text)
        print(*question.answers, sep='\n')
        answer = input('Введите ваш ответ: ')
        sleep(0.5)
        if answer != question.rigth_answer:
            print('Неправильный ответ')
            print(f'правильный ответ {question.rigth_answer}')
            if question.explanation:
                print(question.explanation)
        sleep(5)

if __name__ != '__main__':
    main()