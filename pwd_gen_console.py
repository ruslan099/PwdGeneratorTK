import random
import time

# Создаем алфавит для дальнейшей генерации
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = "!(){}[]_-'?"

# Сцепляем все строки в одну
all = a + b + c + d
length = 8      #Размер пароля


password = "".join(random.sample(all, length))       # Метод sample генерирует случайную строку
print("Идет генерация пароля...")
time.sleep(2)
print(password)