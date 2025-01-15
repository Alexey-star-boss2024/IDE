import numpy as np
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number: int = 1) -> int:
    """Функция угадывания рандомного числа от 1 до 100.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0                                                   # счетчик попыток поиска числа
    min_value, max_value = 0, 101
    predict_number = np.random.randint(1, 101)                  # предполагаемое число
    while True: 
        predict_number != number                                
        count += 1                                              # считаем кол-во попыток найти число с помощью цикла
        if predict_number == number: 
            break                                               # выход из цикла если угадали число
        elif predict_number > number:
            max_value = predict_number                          # уменьшаем диапазон поиска в цикле
            predict_number = (max_value + min_value)//2         # берем середину от нового диапазона и начинаем цикл по новой с целью минимизации кол-ва попыток
        elif predict_number < number:                           
            min_value = predict_number                          # уменьшаем диапазон поиска в цикле 
            predict_number = (max_value + min_value)//2         # берем середину от нового диапазона и начинаем цикл по новой с целью минимизации кол-ва попыток

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)