gridScale = {"x" : 49, 
             "y" : 20}
gridLinesOdd = ["/" ," ","\\","_"]
gridLinesEven = ["\\","_","/"," "]
x = 1
y = 1

while y <= gridScale["y"]:
    gridString = ""
    while x <= gridScale["x"]:
        if y%2 != 0:
            for line in gridLinesOdd:
                if x > gridScale["x"]:
                    break
                else:
                    gridString = gridString + line
                    x += 1
        else:
            for line in gridLinesEven:
                if x > gridScale["x"]:
                    break
                else:
                    gridString = gridString + line
                    x += 1
    print(gridString)
    y += 1
    x = 1