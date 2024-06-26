# Запрос строки у пользователя
user_input = input("Введите строку: ")

# Длина строки в байтах
bytes_length = len(user_input.encode('utf-8'))

# Длина строки в символах
characters_length = len(user_input)

# Вывод результатов
print(f"Длина строки в байтах: {bytes_length} байт")
print(f"Длина строки в символах: {characters_length} символов")
