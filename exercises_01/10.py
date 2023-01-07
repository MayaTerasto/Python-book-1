# Функция, връщаща като резултат сумата на нечетните числа
lst = input("Въведи списък с числа: ")

def sum_of_odds(txt):
    nums = [int(a) for a in txt.split(", ") if int(a) % 2 == 1]
    print(sum(nums))

sum_of_odds(lst)