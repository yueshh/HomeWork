calls = 0
def count_calls():
    global calls
    calls += 1
    return
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

