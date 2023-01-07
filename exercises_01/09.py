# Функция, връщаща като резултат второто по големина число в списъка,
# предаден като аргумент на функцията
lst_input = input("Въведете лист: ")
def show(txt):
    nums = [int(a) for a in txt.split(", ")]
    nums = sorted(nums,reverse=True)
    print(nums[1])
# Извикване на функцията:
show(lst_input)

