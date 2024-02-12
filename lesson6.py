# Функции
'''
def add(a, b):
    result = a + b
    return result
add_result = add(3, 5)
print(add_result)

def brain_fuck(b, a, c):
    result = (b ** 2) - (4 * a * c)
    return result
disc = brain_fuck(3, 5, 7)
print(disc)
print(add_result / disc) # {:.2f} - как это сюда вставить?

a = [1, 2, 3] # a* - оператор рассширения
b = [*a, 4, 5, 6]
print(b)

def print_scores(student, *scores):
    print(f'Имя студента: {student}')
    for score in scores:
        print(score, end=' ')
print_scores('Dima', 12, 25, 13, 95, 54, 78, 94, 62) # как вывести в одну строку?
'''

# def repeat(n):
#     def decorate(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                  func(*args, **kwargs)
#         return wrapper
#     return decorate
# @repeat(5)
# def greet(name):
#     print(f'Привет, {name}!')
#
# greet('Alice')
#
#
# def decorate(func):
#     def wrapper(*args, **kwargs):
#         print('Вызываем функцию')
#         result = func(*args, **kwargs)
#         print('Функция отработала')
#         return result
#     return wrapper
#
# @decorate
# def multiply(a, b):
#     return a * b
# result = multiply(5, 3)
# print(result)

color = 'red'
def print_color():
    global color
    color = 'green'
    return color
print(color)
print(print_color())
print(color)



