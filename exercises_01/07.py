# Изчисляване на n-факториел
n = input("Въведете число: ")
# Променлива с текстова стойност:
txt = "1"
# Индексна променлива:
k = 1
factoriel = 1
if int(n) > 0:
    while str(k) != n:
        k += 1
        factoriel = factoriel * k
        txt = txt +" * "+str(k)
    print("Факториелът на числото", n + " e:", factoriel)
    print(txt + " =", factoriel)
else:
    print("Числото, което сте въвели, не е положително!")
