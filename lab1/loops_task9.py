testSting = "Python — это Питон!"
i = 0

while i < len(testSting):
    for c in testSting:
        i += 1

print(f"В указанной строке {i} символов")