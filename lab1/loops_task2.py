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

testString = ""
testString = GenerateString(10)
for c in testString:
    try:
        int(c)
        print(c)
    except:
        pass

print(testString)