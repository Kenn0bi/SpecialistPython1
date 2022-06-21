# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

# Вариант 1
def lucky_ticket(ticket_number):
    dig_1 = ticket_number // 1000
    dig_2 = ticket_number % 1000
    sum_dig_1 = dig_1 // 100 + (dig_1 % 100 // 10) + dig_1 % 10
    sum_dig_2 = dig_2 // 100 + (dig_2 % 100 // 10) + dig_2 % 10
    return  sum_dig_1 == sum_dig_2

# Вариант 2
def lucky_ticket_v2(ticket_number):
    dig_1 = list(str(ticket_number)[:3])
    dig_2 = list(str(ticket_number)[3:])
    return  sum(map(int, dig_1)) == sum(map(int, dig_2))


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

print(lucky_ticket_v2(123006))
print(lucky_ticket_v2(12321))
print(lucky_ticket_v2(436751))
