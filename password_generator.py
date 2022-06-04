"""
##### Generate a password, with n characters, that has at least
    - 1 uppercase letter
    - 1 lowercase letter
    - 1 special character
    - 1 number
"""
import string
import random


while True:
    try:
        number_chars = int(input("Digite o número de caracteres da senha: "))
    except ValueError:
        print("Por favor, digite um número válido.")
    else:
        break

password_alphabet = string.ascii_letters + string.punctuation + string.digits

system_random = random.SystemRandom()

password_list = [
    system_random.choice(list(string.ascii_uppercase)),  # UPPERCASE_LETTER
    system_random.choice(list(string.ascii_lowercase)),  # LOWERCASE_LETTER
    system_random.choice(list(string.punctuation)),  # SPECIAL_CHARACTER
    system_random.choice(list(string.digits))  # DIGIT_CHARACTER
]

password_list += [system_random.choice(list(password_alphabet))
                  for _ in range(number_chars - 4)]

system_random.shuffle(password_list)
password = "".join(password_list)

print(f"\nSenha gerada com {number_chars} caracteres: {password}\n")
