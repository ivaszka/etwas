from random import randint

# зад3, вар2 Все четные по значению элементы исходного списка A поместить в новый список B
n = input("Enter length of list: \n")
n = int(n)
arrayA = []
arrayB = []
for i in range(n):
    arrayA.append(randint(0, 100))
    if arrayA[i] % 2 == 0:
        arrayB.append(arrayA[i])
print('initial array data: ' + str(arrayA))
print('result array data: ' + str(arrayB))
