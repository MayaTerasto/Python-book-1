# Проверка дали числото се дели на 3:
num = input("Въведете число: ")
result = int(num) / 3
if int(num) % 3 == 0:
    print(num+" : 3 =", result)
else:
    print("Числото",num+" не се дели на 3")