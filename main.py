#                                                #ПЕРЕМЕННЫЕ
# #name =
# #list if elif
#
#                                                 #типы данных
# #string(str) - "123" "hello"
# #integer (int)
# #float bool
#
# #str
# #name = "Kseia"
# #print(type(name))
#
# #int - числовой тип данных от 0 до бесконечности + мат операции
# #num = 10
# #num2 = 20
# #print(num+num2)
# #print(num-num2)
# #print(num*num2)
#
# float - число с плавающей точкой 41.2 123.321
# num = 10.234
# num2 = 20.456
# num3 =num+num2
# print(num+num2)
# print(num-num2)
# print(num*num2)
# print(round(num3,2))
#
# #name = input("Как вас зовут? ")
#
# #методы str
# text = "кыргызстан"
# print(text.title())
# print(text.lower())
# print(text.capitalize())
# print(text.upper())
#
#
# print("здравствуйте я врач")
# name= str(input("Кау вас зовут"))


# num = 11111
# num2 = 1111111
# print(num*num2)
#
# num = 42
# num2 = 4
# num3 = 2
# num4 = -2
# print(num/(num2+num3*num4))



# the_numb = random.randint(1, 100)
# guess = int(input("Назовите число"))
# tries = 1
# while guess != the_numb:
#     if guess > the_numb:
#         print("Меньше")
#     else:
#         print("Больше")
#     guess = int(input("Назовите число"))
#     tries += 1
# print("Вам удалось отгадать число,это в самом деле", the_numb)
# print("На это вам потребовалось", tries, "Попыток")

# import random
# the_numb1 = random.randint(1, 100)
# akinator = (str(input("Загадайте число от 1 до 100")))
# print("Я угадаю ваше число")
# akinator = (int(input()))
# tries = 1
# while akinator != the_numb1:
#      if akinator > the_numb1:
#           print("нет")
#      else:
#           print("да")
# tries += 1
# print("Я смог отгадать число,это в самом деле", the_numb1)
# print("На это мне потребовалось", tries, "Попыток")

# def binary_search(lst, search_item):
#     low = 0
#     high = len(lst) - 1
#     search_res = False
#     while low <= high and not search_res:
#         middle = (low + high) // 2
#         guess = lst[middle]
#         if guess == search_item:
#             search_res = True
#             return search_res
#         if guess > search_item:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return search_res
# lst =
# value =
# result = binary_search(lst, value)
# if result:
#     print("Элемент найден!")
# else:
#     print("Элемент не найден.")

                         # Структура данных list tuple dict - списки кортежи и слов

#text = ["Hello", 123,"inai", 45, True, 32.12,]

# #append,insert
# text.append("projector")
# text.append(123)

# text.insert(2,"hello wprld")
# print(text)

#remove, del
# text.remove(123)
# del text[-1]
# print(text)

#изменение
# text[0] = "I love"
# print(text)

# number = [2,3,5,6,7,11,44,345,667,5678,1]
# number.sort()
# number.reverse()
# print(number)
#
# word = "hello"
# word = list(word)
# word.reverse()
# print(word)

# nominal = (1,3,5,10,35,488,78,2000,1)
# print(type(nominal))
# print(nominal.count(1))
# print(nominal.index(35))
#
# nominal = list(nominal)
# nominal.append("112")
# nominal = tuple(nominal)
# print(type(nominal))
# print(nominal)


#dict - словари
# student = {
#     "name": "Jony"
#     "age" : 18,
#     "hight" : 1.24,
#     "education" : False
# }

# spisok1 = [1,3,5,10,20,200,]
# spisok2 = ["nothing", "nothing", "nothing","nothing", "Т.Сатылганов","А.Oсмонов"]
# print(spisok1)
# print(spisok2)
#
# money = dict(zip(spisok2,spisok1))
# print(money)
#
# for keys, values in money.items():
#     print(f'{keys}-{values}')

# data_types = [1,2,'hello','text',1234]
# data_types2 = []
#
# for i in data_types:
#     if type(i) == str:
#         data_types2.append(i)
# print(data_types2)


                                                      #Задание
# lesson = ('I','L','O','V','E','A','N','I','M','E',True,False,2,1,3,5,4,11,13,12,12,33.222,True,False)
#
# word = []
# number = []
# bollean = []
#
# for i in lesson:
#      if type(i) == str:
#          word.append(i)
#          word.reverse()
#
#
#      if type(i) == int:
#          number.append(i)
#          number.sort()
#      if type(i) == bool:
#          bollean.append(i)
#
# word[1]="L"
# word[4]='I'
# word[9]= 'A'
#
# tuple1 = tuple(word)
# tuple2 = tuple(number)
# tuple3 = tuple(bollean)
# print(tuple1)
# print(type(tuple1))
                    # print(tuple2)
# print(type(tuple2))
# print(tuple3)
# print(type(tuple3))
# print(word)
# print(number)
# print(bollean)

# INAI = {
#     'address': 'Toktogula 175',
#     'courses': ['Android','Backend','Frontend'],
#     'bag':{'fails','errors','stack'},
# }
# del INAI['bag']
# INAI['address'] = 'Maldibaeva 34'
# INAI['instagram'] = 'inai.kg'
# INAI['phone number'] = '055396594'
# INAI['courses'] = 'Android','Backend','Frontend', 'English', 'Germany'
# print(INAI)
#
# for key, value in INAI.items():
#   print(key, '->', value)


                                               # if elif else.Теория

# time = str(input('Когда вы проснулись? '))
# if time == "утром" :
#     print(f'Вы вы проснулись в {time} вы успеете на учёбу! ')
#
# elif time>='Поздно утром' and time<= 'за 9' :
#     print(f'Вы проснулись в {time} Вы пойдёте на учёбу?')
#     answer = str(input('Введите ответ да/нет'))
#     if answer == 'да' :
#         print(f'Ваш ответ {answer} Вы молодец!')
#     elif answer == 'нет' :
#         print(f'Ваш ответ {answer} Вы не молодец!')
#     else:
#         print('Мне ко второй')
#
#
# elif time == 'обед':
#     print('вас отчислили!')

# for i in 1,33,'querty','hello',True :
#     print(i)

# box = 20
# box2 = 0

# while box != 0:
#     box -=1
#     box2 +=1
#     print(f'C первого бокса {box}')
#     print(f'Со вторго бокса {box2}')



                                               #функции.Теория

# def square(a , b):
#     print(a*b)
#
# square(12, 21)
# square(321, 123)

# def greeting(name):
#     print(f'Hello{name}')\
#
# greeting(str(input('Введите имя 1 ')))
# greeting(str(input('Введите имя 2 ')))
# greeting(str(input('Введите имя 3 ')))

#return
# def summa(a,b,c):
#     return (a+b+c)/3
# print(summa(1,3,1))
# a = summa(1,3,44)
# print(a)

# def plus(a,b,c=12):
#     return a+b+c
# print(plus(2,3))

# def average(*args):
#     return sum(args)/len(args)
# print(average(1,2,3,4,5,6,7,8,7,56,65,44567))


# def menu(**kwargs):
#     return kwargs
#
# eat = menu(morning="Бекон с яйцом", lunch="Лагман с говядиной", diner="Плов с мясом")
# print(type(eat))
#
# try:
#     a = "12"
#     b = 12
#     print(a+b)
# except:
#     print("Зачем?")


# univer = list()
# technikum = list()
# army = list()
# married = ()
#
#
# abiturients = [
#     {'name':'Baitemir', 'ORT':110, 'gender':'male'},
#     {'name':'Frederic', 'ORT':130, 'gender':'male'},
#     {'name':'Aikanysh', 'ORT':210, 'gender':'female'},
#     {'name':'Oleg', 'ORT':170, 'gender':'male'},
#     {'name':'Malika', 'ORT':20, 'gender':'female'},
# ]
#
# def all_abits(lst):
#     for i in lst:
#         for key, value in i.iteams():
#             print(f'{key}-{value}')
#
#
# def selecion(lst, univer:list,techbikum:list, army:list, married:list):
#     if i in lst:
#         for i['ORT']>=110:
#             univer.append(i)
#     elif i['ORT']<=109 and i['ORT']>=80:



#Задание
# sport_car = []
# modern_car = []
# old_car = []
#
# europe_car = []
# asian_car = []
# american_car = []
# russian_car = []

# cars = [
#     {'title' : 'BMW', 'Countri':'Europe', 'volume':3.0,'type':'sport'},
#     {'title' : 'Mersedes', 'Countri':'Europe', 'volume':4.0,'type':'modern'},
#     {'title' : 'Honda', 'Countri':'Asian', 'volume':3.5,'type':'modern'},
#     {'title' : 'Ferari', 'Countri':'American', 'volume':7.0,'type':'sport'},
#     {'title' : 'Lada', 'Countri':'Russian', 'volume':4.0,'type':'old'},
# ]
#
# def all_cars(lst):
#     for i in lst:
#         for key,value in i.items():
#             print(f'{key} - {value}')
# all_cars(cars)
#
# def selection(lst,sport_car:list, modern_car:list, old_car:list, europe_car:list,asian_car:list,american_car:list,russian_car:list ):
#     for i in lst:
#         if i['Countri'] == 'Europe':
#             europe_car.append(i)
#         elif i['Countri'] == 'Asian':
#             asian_car.append(i)
#         elif i['Countri'] == 'American':
#             american_car.append(i)
#         elif i['Countri'] == 'Russian':
#             russian_car.append(i)
#     for i in lst:
#         if i['type'] == 'sport':
#             sport_car.append(i)
#         elif i['type'] == 'old':
#              old_car.append(i)
#         elif i['type'] == 'modern':
#              modern_car.append(i)
#
#
#
# selection(cars ,sport_car,modern_car,old_car,europe_car,asian_car,american_car,russian_car)
# print('-'*20)
# print(f'American - {american_car}\n'
#       f'Asian = {asian_car}\n'
#       f'Russian - {russian_car}\n'
#       f'Europe - {europe_car}\n'
#       f'Modern = {modern_car}\n'
#       f'Sport - {sport_car}\n'
#       f'Old - {old_car}\n'
#       )





