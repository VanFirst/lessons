#list = [1, 2, 3, 'Hello', True, False]
#print(list)
#print(list[1])
#print(id(list[2]))
#list[1] = 7
#print(list)
#print(list[0:6:2]) #последний элемент не попадает (срез)!
#for i in list:
#    print(i, end=' ')

#cross = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(cross)
#print(cross[2][1], cross[1][0]) #обращение к конкретному элементу


#data = [i for i in range(0, 1000)]
#print(data)

#print(data)
#count = 0
#for i in data:
#    count+= 1 #count = count + 1
#print(count)

#a = (1, 2, 3)
#b = [1, 2, 3]
#print(a.__sizeof__())
#print(b.__sizeof__())

#first_tuple = (1, 2, 3)
#second_tuple = (4, 5, 6)
#print(first_tuple + second_tuple)
#print(sum(first_tuple + second_tuple))

#companies = {'BMW', 'Lada', 'KFC'}
#tech_companies = ['Apple', 'Xiaomi', 'ZTE']
#companies.update(tech_companies)
#print(companies)




'''
#Списки - изменяемые упорядоченные объекты в квадратных скобках. Первый 0.
list_names = ['1', '3.14', 'Ann', '[100, 101]']
list_names[2] = 'Van'
#print(list_names)
b = list_names[0:2] #не включая третий элемент!!!
#print(b)
c = list_names[2:] #тут уже до последнего включительно!
#print(c)
#list_names[0:2] = ['Dave','Mark','Jeff']???
#print(list_names)???
list_names2 = ['2' , '4.345' , 'Devid']

L1 = list_names
L2 = list_names2
#print(L1 + L2)

#L1.extend(L2)#объединение списков
#print(L1)

#print(('!'.join(L1 + L2)))#разделитель!!!

L1.append('Asgard')#добавляет в конец списка!
#print(L1)

L1.pop(-1)#удаляет! Можно ничего не писать - удалит последний элемент.
#print(L1)

L1.remove('Van')#Удаляет и не возвращяет!!!

L1.insert(1, 2)#вставляет элемент на определенное место.

#print(L1)

#L1.sort()
#sorted(L1) сортирует
#print(L1) #переключать строки как?

#как можно красиво разделять всё , что написано?

a = [1, 2, 3, 4]
a[0:2]
print(a)            # полуим [1, 2] почему? шаг элементов???

print(L1 == L2)
len(L1)         #как это вывести?
#min(L1) , max(L1)
'''



'''
#генерация списков
list = [i for i in range(0, 10)]
print(list)
list = [i for i in range(0, 10) if i % 2 == 0]
print(list)

list = [i * j for i in range(0, 3) for j in range(0, 3)] #как это работает?
print(list)

data = [[i * j for i in range(0 , 3)] for j in range (0, 3)] # Двумерная матрица 3х3
print(data)
'''


'''
# Кортежи - не изменяемые упорядоченные объекты в круглых скобках. Нельзя изменять после создания! Начинается с 0!
# Из чисел, строк, лог. значений, др. кортежей, списков, словарей и разных тип. данных.
cortege = (1, 2, 3, 4, 5, 8, 9, 14, 44, 33)
#print(cortege)
#cortege[0][1] = 10  #???
#first = cortege[0]
#print(first)
#second_to_last = cortege[-2]
#print(second_to_last)

#for element in cortege: #Перебор элементов
    #print(element)
#i = 0

#while i < len(cortege): # Как это работает?
    #print(cortege[i])
    #i += 1

#new = cortege * 3
#print(new)

#sum = sum(cortege)
#print(sum)

sorted_cortege = tuple(sorted(cortege)) #сортировка, или tuple(sorted(cortege, reverse=True))
print(sorted_cortege)

cortege = (1, 2, 3) # Преобразование кортежа в список
list = list(cortege)
print(cortege)
print(list)
'''



# Множества - set {}
empty_set = set()
print(set)