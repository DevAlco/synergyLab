first = 0
second = 0

while True:
    try:
        first = float(input("Введите первое число: "))
        break
    except:
        print("Вы ввели неправилное число")
    
while True:
    try:
        second = float(input("Введите второе число: "))
        break
    except:
        print("Вы ввели неправилное число")
    
try:
    crossproduct = first / second
except ZeroDivisionError:
    print("На ноль делить нельзя")
except:
    print("Что-то пошло не так")
else:
    print(f"Произведение {first} и {second} равно {crossproduct}")