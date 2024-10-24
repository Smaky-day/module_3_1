calls = 0   # переменная вне функций
def count_calls():  # 1ая функция: подсчитывает вызовы остальных функций
    global calls   # обращаться будем к глобальной переменной
    calls += 13  # увеличиваем значение переменной calls на 13 каждый раз при вызове

def string_info(string):  # 2ая функция: принимает аргумент и возвращает кортеж
    count_calls()  # зададим пустую строку
    length = len(string)  # вычислим длину string
    upper_case = string.upper()  # преобразуем эту строку в верхний регистр
    lower_case = string.lower()  # преобразуем эту строку в нижний регистр
    return length, upper_case, lower_case   # вернем все 3 эти значения

def is_contains(string_, list_): # 3тья функция: принимает 2 аргумента и возвращает True/False
    count_calls()  # зададим пустую строку
    StringLower = string_.lower()   # преобразуем string в нижний регистр
    for element in list_:
        if StringLower == element.lower():  # если строка StringLower ровна element в нижнем регистре, то True
            return True
    return False   # цикл заверщён, а ни один элемент не совпал, то False

print(string_info("Не выходи из комнаты; считай, что тебя продуло."))
print(string_info("Что интересней на свете стены и стула?"))
print(string_info("Зачем выходить оттуда куда, вернешься вечером"))
print(string_info("таким же, каким ты был, тем более - изувеченным?"))
print(is_contains("Поэтессы", ["Ахматова", "Цветаева"]))
print(is_contains("цветы", ["незабудки", "ромашки", "цветы"]))
print(is_contains("НЕ были", ["Будь", 'тем, чем', 'другие', "не были"]))

print(f"{calls}")  # количество вызовов * 13