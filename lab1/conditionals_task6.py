while True:
    try:
        number = int(input("Введите натуральное число: "))
        break
    except:
        print("Вы ввели неправилное число")
        
if number%3 == 0:
    print(f"Число {number} кратно трем.")
else:
    print(f"Число {number} не кратно трём")