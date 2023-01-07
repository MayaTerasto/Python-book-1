# Последователност на Фибоначи
n = input("Въведете число: ")

number = 0
lst = [1, 1]
while len(lst) != int(n):
    number = lst[-1] + lst[-2]
    lst.append(number)

print(lst)