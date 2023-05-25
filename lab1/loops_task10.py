checkList = [(1, 2), (3), (4,), (5+6), (7+8,)]
tuppleList = []

for value in checkList:
    if isinstance(value, tuple):
        tuppleList.append(value)
        
print(tuppleList)