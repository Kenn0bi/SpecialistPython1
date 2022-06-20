# Напишите функцию находящую n-ое число Фибоначчи.

def fibonacci(n):
    num_fib = 0
    num_fib_prev = 0
    i = 0

    while i < n:
        if i == 1:
            num_fib = 1
        else:
            num_fib += num_fib_prev
            num_fib_prev = num_fib - num_fib_prev
        i += 1
    return num_fib


n = int(input("Введите целое положительное число: "))

print(f"{n}-ое число Фибоначчи: {fibonacci(n)}")
