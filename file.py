print("Hello World")

x = list('список');
print(x)

# шикарные циклы
count = 0

print("while")

while count < 100:

    print(count)

    count += 20

# левый неведомый массив)))
array = [4,5,2,7,4,3,5,56,109,4]

print("for")

n = 10

for i in array:

    l = n * i # ; <- уже на автомате ставлю ; Это - проклятие плюсов)))) Можно такой фильм снять "Проклятие плюсов" Сорян, настроение хорошее)))

    print(l)


# Божественные числа Фибоначи
# fibNumbers1 = fibNumbers2 =  1
fibNumbers1 = 1
fibNumbers2 = 1

n = input("Введите номер ряда числа Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    fibSumma = fibNumbers1 + fibNumbers2
    fibNumbers1 = fibNumbers2
    fibNumbers2 = fibSumma
    i = i + 1

print("Число Фибоначи", fibNumbers2)





# поиск по левому неведомому массиву
print("Бинарный поиск")
for i in array:
    if i == 7:
        print("Ура нашли!!!")

# бинарный поиск по левому неведомому массиву по рекурсии с помощью функции
num = 4
# def Bynary_poisk(arr, num):
first = 0
last = len(array)-1
index = -1
while (first <= last) and (index == -1):
    mid = (first+last)//2
    if array[mid] == num:
        index = mid
    else:
         if num < array[mid]:
            last = mid -1
         else:
            first = mid +1

print(index)
    # return index




# f ntgthm aeyrwbz!!!!!
def Bynary_poisk(arr, num):
    first = 0
    last = len(array)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if array[mid] == num:
            index = mid
        else:
            if num < array[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

>>> Bynary_poisk([2, 2, 3, 6, 7, 7], num)



# >>> print(Bynary_poisk([10,20,30,40,50], 20))
