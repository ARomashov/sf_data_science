def game_core_v3(number: int = 1) -> int:
    """
    Угадываем число с помощью алгоритма бинарного поиска
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Реализуем алгоритм бинарного поиска для решения задачи
    count = 0
    start, end = 1, 100 # Начальная и конечная границы множества 
    predict = int(end / 2) # Начинаем с центрального элемента множества

    while number != predict:
      count += 1
      # Если число в левой половине, то сдвигаем конечную границу, если в правой, то начальную
      if predict > number:
        end = predict - 1
      else:
        start = predict + 1
      predict = start + int((end - start) / 2) # Выбираем серединный элемент полученного множества
    # Ваш код заканчивается здесь

    return count