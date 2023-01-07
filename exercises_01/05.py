n = int(input("Въведете горна граница: "))
num = [5 * k + 3 for k in range(n)]
print("По възходяща стойност:",num)
print("По низходяща стойност:", list(sorted(num,reverse=True)))

