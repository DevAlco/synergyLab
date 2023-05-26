testDict = { "key1":"Value1" , "key2":"Value2", "key3":"Value3", "key4":"Value4" }
i = 0
for key,value in testDict.items():
    if key == "key1":
        if value == "Value1":
            print(f"{key} {value}")
            break
        else:
            print("Неверное значение ключа")
            break
    i += 1

if i >= len(testDict):
    print("В словаре нет указанного ключа")