testDict = { "key1":"Value1" , "key2":"Value2", "key3":"Value3", "key4":"Value4" }
testList = ["f3", "7h", "key10", "key3", 4, "farro", "key1"]
matchList = []

for item in testList:
    for key,value in testDict.items():
        if key == item:
            matchList.append(value)
        
print(matchList)