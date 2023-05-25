import random,string

def GenerateValuesList(lenght):
    random.seed()
    i = 0
    tempValues = []
    for i in range(0, lenght):
        if i == random.randint(0, 10):
            tempValues.append(random.randint(-10000,10000))
        else:
            tempValues.append(random.choice(string.ascii_letters))   
    return tempValues

checkList = GenerateValuesList(10)

for value in checkList:
    if isinstance(value, int):
        print(value)

print(checkList)