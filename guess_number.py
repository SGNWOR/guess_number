from random import randint as rd

random = rd(1, 100)

print('Угадай число от 1 до 100!')

def main():
while True:
    your_value = int(input('Введите число от 1 до 100: '))
    
    if your_value == random:
        break
    elif your_value < random:
        print('Нужное число больше вашего!')
    elif your_value > random:
        print('Нужное число меньше вашего!')    