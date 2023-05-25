import random

def GenerateNumList(lenght):
    random.seed()
    i = 0
    tempNums = []
    for i in range(0, lenght):
        tempNums.append(random.randint(-10000,10000))   
    return tempNums

checkList = GenerateNumList(10)

for num in checkList:
    if num >= 0:
        print(num)
        
print(checkList)