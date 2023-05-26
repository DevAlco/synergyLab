testString ="""Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.\n 
Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage,\n 
and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum"\n 
(The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance.\n 
The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.\n
The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.\n 
Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form,\n 
accompanied by English versions from the 1914 translation by H. Rackham."""

forbiddenList = ["latin", "from", "literature", "undoubtable"]
#forbiddenList = ["Вася"]
    
splitTestString = testString.split(' ')
i = 0
forbiddenfound = False
for word in splitTestString:
    i += 1
    if forbiddenfound:
        break
    else:
        for forbiddenWord in forbiddenList:
            if word.lower() == forbiddenWord:
                print(f"Найдено запрещённое слово: {forbiddenWord}, в тексте!")
                forbiddenfound = True
                break
            elif i == len(splitTestString):
                print("Запрещённых слов не обнаружено")