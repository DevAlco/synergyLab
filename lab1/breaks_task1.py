userInput = input("Введите последовательность чисел: ")
i = 0
for c in userInput:
    try:
        int(c)
        i += 1
    except:
        print("Вы ввели не только числа!")
        break

if i == len(userInput):
    print("Все в порядке!")
