import random,string

def GenerateString(lenght):
    random.seed()
    i = 0
    randString = ""
    tempString = ""
    tempString= tempString + string.digits + string.ascii_letters
    for i in range(0, lenght):
        randString = randString + random.choice(tempString)
    return randString

testStringBase = GenerateString(10)
testStringModified = ""

for c in testStringBase:
    for i in range(0,3):
        testStringModified = testStringModified + c
        i += 1

print(f"Исходная строка: {testStringBase}")
print(f"Модифицированная строка: {testStringModified}")