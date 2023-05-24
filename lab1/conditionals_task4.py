import string,random

def GenerateString(lenght, upperCase):
    random.seed()
    i = 0
    randString = ""
    if upperCase == "y" or upperCase == "Y":
        for i in range(0, lenght):
            randString = randString + string.ascii_letters[random.randint(0,len(string.ascii_letters))]
    else:
        for i in range(0, lenght):
            randString = randString + string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase))]
    return randString


i = 0
randString = GenerateString(5, "Y")

print(randString)

for c in randString:
    if c == "A" or c == "a":
        print(f"В строке есть {c}")
        i += 1
    elif c == "B" or c == "b":
        print(f"В строке есть {c}")
        i += 1
    elif c == "C" or c == "c":
        print(f"В строке есть {c}")
        i += 1
        
if i == 0:
    print("В сроке нет нужной буквы")