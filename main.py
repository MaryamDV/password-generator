import random
list_numbers = "1234567890"
list_letter = "qwertyuiopasdfghjklzxcvbnm"
list_letter = list_letter + list_letter.upper()
list_symbols = "!@#$%^&*()?|/~"
list_all = list_numbers + list_letter + list_symbols
pas_len = int(input("Какой длинны хотите пароль?"))

for j in range (10):
    password = ""
    for i in range(pas_len):
        password += random.choice(list_all)
    print("Ваш пароль:", password)
    
