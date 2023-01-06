# Функция за изобразяване на буквите от предаден като аргумент текст:
def show(txt):
# Преобразуване на текста в списък и сортиране:
    symbs = sorted(list(txt))
# Показване съдържанието на списъка:
    print(symbs)
# Извикване на функцията:
show("Python")

# Функция за изчисляване сумата на квадратите на естествените числа:
def sqsum(n):
# Създаване на списък от квадратите на естествените числа:
    nums = [k * k for k in range(1, n+1)]
# Резултат от функцията:
    return sum(nums)
# Променлива с числова стойност:
m = 10
# Извикване на функцията за изчисление на сумата от квадратите на числа:
print("Сумата на квадратите на числата от 1 до", str(m)+":", sqsum(m))
