hour = int(input("Введите часы:"))
minutes = int(input("Введите минуты:"))
if hour < 24 and minutes < 60:
    print("Числа могут быть временем.")
else:
    print("Числа не могут быть временем.")
