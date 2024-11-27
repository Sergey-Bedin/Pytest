import random

answer = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]


def game_again():
    while True:
        ans = input("Продолжаем? (да, нет)").lower()
        if ans == "да":
            return True
        elif ans == "нет":
            return False
        else:
            print("Я не понял, напиши еще раз")
            continue


flag_game = True
while flag_game:
    input("Каков вопрос? \n")
    print(random.choice(answer))
    flag_game = game_again()
