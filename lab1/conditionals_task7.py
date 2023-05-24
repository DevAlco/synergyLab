import random

random.seed()
first = random.randint(-100, 100)
second = random.randint(-100, 100)
third = random.randint(-100,100)
print(f"Даны числа: {first} {second} {third}")

if first > second:
    if first > third:
        print(f"{first} наибольшее число")
    else:
        print(f"{third} наибольшее число")
elif second > third:
    print(f"{second} наибольшее число")
else: 
    print(f"{third} наибольшее число")

