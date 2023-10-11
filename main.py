#def distance(x1, y1, x2, y2):
#    dst = ((y2 -y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#    return dst
#print(distance(int(input()), int(input()), int(input()), int(input())))

#def power(a, n):
#    num = 1
#    if n >= 0:
#        for i in range(n):
#            num *= a
#            return num
#    else:
#        a = 1 / a
#        for i in range(-n):
#            num *= a
#    return num
#print(power(int(input()),int(input())))

# def fib(n):
#    if n in (1, 2):
#        return 1
#    return fib(n - 1) + fib(n - 2)
# print(fib(int(input())))

# def is_year_leap(year):
#     if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
#         return True
#     else:
#         return False
# print(is_year_leap(int(input())))

# def square(a):
#     import math
#     p = a * 4
#     s = a * a
#     d = a * math.sqrt(2)
#     return p,s,d
# print(square(int(input())))

# def season(month):
#     if month == 12 or month == 1 or month == 2:
#         return 'Зима'
#     elif month == 3 or month == 4 or month == 5:
#         return 'Весна'
#     elif month == 6 or month == 7 or month == 8:
#         return 'Лето'
#     elif month == 9 or month == 10 or month == 11:
#         return 'Осень'
#     else:
#         return 'Не время года'
# print(season(int(input())))

# def bank(a,years,procent):
#     for i in range(years):
#         a *= procent
#     num = a
#     return num
# print(bank(int(input()),int(input()),float(1.1)))

# def is_prime(a):
#     if a > 1000 or a < 0:
#         return 'Не правильно'
#     elif a % 2 == 1:
#         return 'Число простое'
#     elif a % 2 == 0:
#         return 'Число не простое'
# print(is_prime(int(input())))

# def date(day,month,year):
#     if day < 1 or day > 31:
#         return False
#     if month < 1 or month > 12:
#         return False
#     if year < 1:
#         return False
#     if day > 30:
#         return False
#     return True
# print(date(int(input()),int(input()),int(input())))