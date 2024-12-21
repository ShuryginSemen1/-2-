import random

def play_guess_the_number():
    """Запускает игру 'Угадай число'."""

    secret_number = random.randint(1, 10)
    attempts_left = 3

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 10. У вас есть 3 попытки, чтобы угадать его.")

    while attempts_left > 0:
        try:
            guess = int(input(f"Попытка {4 - attempts_left}: Введите ваше предположение: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
            continue

        if guess == secret_number:
            print(f"Поздравляю! Вы угадали число {secret_number}!")
            return # Завершаем игру, если угадали

        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

        attempts_left -= 1

    print(f"Вы проиграли. Загаданное число было {secret_number}.")

if __name__ == "__main__":
    play_guess_the_number()
