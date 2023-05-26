testDict = { "key1":"Value1" , "key2":"Value2", "key3":"Value3", "key4":"Value4" }
i = 0
for key in testDict.keys():
    if i%2 == 0:
        print(key)
    i+=1