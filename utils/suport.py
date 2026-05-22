import os

def get_number_value(msg):
    while True:
        try:
            var = input(msg)

            return float(var)
        
        except ValueError:
            input('Digite um valor numerico \n---Pressione ENTER---')
            clear()

def clear():
    os.system('cls')

def pagination():
    input('\n---Pressione ENTER---\n')
    clear()