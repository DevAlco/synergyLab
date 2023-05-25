import random

def GenerateNumList(lenght):
    random.seed()
    i = 0
    tempNums = []
    for i in range(0, lenght):
        tempNums.append(random.randint(-10000,10000))   
    return tempNums

nums1 = []
nums2 = GenerateNumList(10)

for num in nums2:
    if num%2 == 0:
        nums1.append(num)

print(f"значения в первом списке: {nums2}\nЗначения во втором списке: {nums1} ")