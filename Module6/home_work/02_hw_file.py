# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

def isnum(s):
    try:
        int(s)
        return True
    except:
        return False


with open("data/info.txt", "r") as f:
    summa = 0
    for line in f:
        if isnum(line.strip()):
            summa += int(line)

print(summa)
