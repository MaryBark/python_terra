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