import random

print("Добро пожаловать в числовую угадайку")
print("Я загадал целое число от 1 до 100, попробуй его угадать")


def is_valid(num):
    if num.isdigit():
        if not float(num) in range(1, 101):
            print("Может постараешься ввести целое число от 1 до 100?")
            return True
        else:
            return False
    else:
        print("Может постараешься ввести целое число от 1 до 100?")
        return True


def game(test_number):
    number = random.randint(1, 100)
    counter = 1

    while True:
        while is_valid(test_number):
            test_number = input("Введи число: ")
            counter += 1
            continue
        test_number = int(test_number)
        if test_number > number:
            print("Мое число меньше:(")
        elif test_number < number:
            print("Мое число больше:)")
        else:
            print("Поздравляю, ты угадал!!!)))")
            print("Попыток понадобилось: ", counter)
            break
        test_number = input("Попробуй еще раз: ")
        counter += 1


flag_again = True
while flag_again:
    test_number = input("Введи число: ")
    game(test_number)
    while flag_again:
        q_again = input("Сыграем еще раз?(да ил нет): ")
        if q_again == "нет":
            print("Ладно, пока(")
            flag_again = False
        elif q_again == "да":
            print("Ооо, отлично)")
            break
        else:
            print("Не пон")

    continue
