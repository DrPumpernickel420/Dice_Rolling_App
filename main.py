from draw import draw_nums
from print import return_dices

print("_______________Dice Rolls _______________")
while True:
    num = input("Type in number of rolls or click Enter to exit: ")
    if num == "":
        break
    else:
        if num.isdigit():
            number = int(num)
            rolls = draw_nums(number)
            print(return_dices(rolls))
        else:
            print("Input is not a number")
            pass

