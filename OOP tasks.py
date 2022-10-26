
# class Person:
#     def __init__(self, name, age, hobby, number):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#         self.number = number
#
#      def speak(self,language):
#         if language == "Russian":
#             return f'Меня зовут {self.name} Я говорю на {language} я живу в Японии'
#         elif language == "English":
#             return f'Меня зовут {self.name} Я говорю на {language} я живу в Англии'
#         else:
#             return f'Я не живу тама'
#
#
#
#
#     def __str__(self):
#         return f'Имя - {self.name}\n'\
#                f'Возраст- {self.age}\n' \
#                f'Хобби- {self.hobby}\n' \
#                f'Номер- {self.number}\n'\
#
# human1 = Person("Lolli", 25, "swiming", 345)
# human2 = Person("Mark", 15, "flying", 3785)
# print(human1)
# print(human2)
# print(human1.speak(str(input('На каком языке вы говорите?'))))



                                                                 #Задание1
# class Ingridients:
#     def __init__(self, vegetable1, vegetable2, vegetable3, fruit, spice, sauce, herbs, utensils, macaroni, cheese ):
#         self.vegetable1 = vegetable1
#         self.vegetable2 = vegetable2
#         self.vegetable3 = vegetable3
#         self.fruit = fruit
#         self.spice = spice
#         self.sauce = sauce
#         self.herbs = herbs
#         self.utensils = utensils
#         self.macaroni = macaroni
#         self.cheese = cheese
#
#
#     def __str__(self):
#         return f'{self.vegetable1}\n' \
#             f'{self.vegetable2}\n' \
#             f'{self.vegetable3}\n' \
#             f'{self.fruit}\n' \
#             f'{self.spice}\n' \
#             f'{self.sauce}\n' \
#             f'{self.herbs}\n' \
#             f'{self.utensils}\n' \
#             f'{self.macaroni}\n' \
#             f'{self.cheese}\n'
#
#     def whatUcook(self, food):
#         if food == "Паста":
#             return f'Сегодня вы готовите {food} поэтому вам нужно {self.macaroni}'
#         elif food == "Пицца":
#             return f'Сегодня вы готовите {food} поэтому вам нужно {self.sausage}'
#         else:
#             return f'У нас есть ингридиенты только для пасты и пиццы'
#
#
# class Pasta(Ingridients):
#      def __init__(self, vegetable1, vegetable2, vegetable3, fruit, spice, sauce, herbs, utensils, macaroni, cheese, spice2, meet):
#          super().__init__( vegetable1, vegetable2, vegetable3, fruit, spice, sauce, herbs, utensils, macaroni, cheese)
#          self.spice2 = spice2
#          self.meet = meet
#
#
#      def __str__(self):
#          return super(Pasta, self).__str__()+f'{self.spice2}\n' \
#                                                      f'{self.meet}'\
#
#
#
# class Pizza(Ingridients):
#     def __init__(self, vegetable1, vegetable2, vegetable3, fruit, spice, sauce, herbs, utensils, macaroni, cheese ,sausage, mushrum):
#         super().__init__(vegetable1, vegetable2, vegetable3, fruit, spice, sauce, herbs, utensils, macaroni, cheese)
#         self.sausage = sausage
#         self.mushrum = mushrum
#
#     def __str__(self):
#         return super(Pizza, self).__str__() + f'{self.sausage}\n' \
#                                               f'{self.mushrum}' \
#
# print("Добро пожаловать в магазин!Какие товары вам нужны?")
#
#
#
#
#
# salesman = Ingridients( "картошка","марковка","помидор","яблоко","соль","тартар", "базилик","печка либо сковорода","спагетти","сыр ламберг")
# cookman1 = Pasta("картошка","марковка","помидор","без яблок","соль","базилик","сковородка","спагетти","сыр ламберг","томатный соус", "перец","говядинна")
# cookman2 = Pizza("картошка","марковка","помидор","без яблоко","соль","базилик","печка","без спагетти","сыр ламберг","сырный соус", "салями","шампиньёны")
# print("                          Мне нужны :   ")
#
# print(cookman1)
# print("                        А мне нужны :   ")
# print(cookman2)
# print(cookman2.whatUcook(str(input('Что сенодня готовим? '))))
# print(cookman1.whatUcook(str(input('А ты что сенодня готовишь? '))))



                                                                #Задание2
# class JunDev:
#     def __init__(self, name, age, language ):
#          self.name = name
#          self.age = age
#          self.language = language
#
#
#     def __str__(self):
#          return f'Имя - {self.name}\n'\
#                 f'Возраст- {self.age}\n' \
#                 f'Язык.прог- {self.language}\n'
#
#
#
#     def education(self,stude_placce ):
#         if stude_placce == "Школа":
#             return f'Вам стоит записаться на курсы'
#         elif stude_placce == "Курсы программирования":
#             return f'Отличная база!'
#         else:
#             return f'Тоже пойдёт!'
#
#     def work(self, company):
#         if company == "Google":
#             return  f'О, да вы из {company}! Богатые родители или просто умный? '
#         elif company == "Местная компания":
#             return f'O,это {company}! Неплохое начало!'
#         else:
#             return f'Быть безработным не стыдно!'
#
#
# worker1 = JunDev("Пётр", 17,"Python")
# print(worker1)
# print(worker1.work(str(input("Где вы работаете?"))))
# print(worker1.education(str(input("Где вы проходили обучение?"))))
#
# class MidDev(JunDev):
#     def __init__(self,name, age, language,country, stage,recomendation):
#         super(MidDev, self).__init__(name, age, language)
#         self.country = country
#         self.stage = stage
#         self.reromendation = recomendation
#
#     def __str__(self):
#         return super(MidDev, self).__str__()+f'{self.country}\n' \
#                                               f'{self.stage}\n'\
#                                                 f'{self.reromendation}\n'\
#
#     def job(self,vocation):
#         if vocation == "Бэкенд":
#             return f'Вы специализируетесь на {vocation}? Вам к нам!'
#         else:
#             return f'Вы нам не подходите!'
#
# worker2 = MidDev("Алиса", 23,"Python", "Англиля", "5 лет","Есть")
# print("-"*20)
# print(worker2)
# print(worker2.job(str(input("Кем вы бы хотели у нас работать?"))))
#
# class SenDev(MidDev):
#     def __init__(self,name, age, language,country, stage,recomendation,workplace,eye_color,sername):
#         super(SenDev, self).__init__(name, age, language,country, stage,recomendation)
#         self.workplace = workplace
#         self.eye_color = eye_color
#         self.sername = sername
#
#     def __str__(self):
#         return super(SenDev, self).__str__()+f'{self.workplace}\n' \
#                                               f'{self.eye_color}\n'\
#                                                 f'{self.sername}\n'\
#
#
#     def money(self,salary):
#         if salary <= 3500:
#             return f'Вы хотите получать {salary} за работу? Вам к нам!'
#         elif salary >= 3500:
#             return f'А вы не обнаглели?'
#         else:
#             return f'Нормально отвечайте ёмаё!'
#
#
# worker3 = SenDev("Эдуард", 34 ,"Java", "Цвикау", "10 лет","Есть","Google company","Зелёный","Альбертович" )
# print("-"*20)
# print(worker3)
# print(worker3.money(int(input("Сколько вы хотите зарабатывать?"))))






#1
class Anime:
    def __init__(self,hobby):
        self.hobby = hobby

    def interest(self):
        return f"Он отаку, потому что любит {self.hobby}"

class Dorama:
    def __init__(self,hobby):
        self.hobby = hobby

    def interest(self):
        return f"Он дорамщик, потому что любит {self.hobby}"

class Book:
    def __init__(self,hobby):
        self.hobby = hobby

    def interest(self):
        return f"Он книжный червь, потому что любит {self.hobby}"

anime = Anime('аниме,например Наруто')
dorama = Dorama('дорамы,например Пентхаус ')
book = Book('книги, например Тихий Дон')

print(anime.interest())
print(dorama.interest())
print(book.interest())



#2
class Instagram:
    def __init__(self, nikname, email, password):
        self.nikname = nikname
        self.email = email
        self.__password = password

    def __str__(self):
        return f'nikname - {self.nikname}\n'\
               f'email - {self.email}\n'\
               #f'password - {self.password}'

inst = Instagram(nikname="mmorkkovkaa", email="lllllooovvvvvee@gmail.com", password="123234345")
print('-'*20)
print(inst)
print('-'*20)



#3
class Book:
    def __init__(self, title,year, color):
        self.title = title
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.title}\n' \
               f'{self.year}\n' \
               f'{self.color}'


class Childrensbook(Book):
    def __init__(self, title, year, color):
        super().__init__(title, year, color)

    def __str__(self):
        return super(Childrensbook, self).__str__()

class Romanticbook(Book):
    def __init__(self, title, year, color):
        super().__init__(title, year, color)
    def __str__(self):
        return super(Romanticbook, self).__str__()

class Teenbook(Childrensbook, Romanticbook):
    def __init__(self, title, year, color):
         super().__init__(title, year, color)
    def __str__(self):
      return super(Teenbook,self).__str__()

b = Book(title="all", year="all", color="all")
c = Childrensbook(title="Сказки", year="от 3 лет",color="rainbow")
r = Romanticbook(title="Про любовь", year="от 25 лет", color="red,black,pink")
t = Teenbook(title="Для подростков", year="от 16 лет", color="light color")

print(b)
print(c)
print(r)
print(t)
print("-"*20)



#4
class Manga:
    def __init__(self, title, year,genr ):
        self.title = title
        self.year = year
        self.genr = genr


    def __str__(self):
        return f'{self.title}\n' \
               f'{self.year}\n' \
               f'{self.genr}'

    def read(self):
        return f'it can be good for girl and boy'

class Anime1(Manga):
    def __init__(self, title,year, genr):
        super().__init__(title, year, genr)
    def __str__(self):
        return super(Anime1, self).__str__()

anime_1 = Anime1(title='Naruto', year=2005, genr="Senen")
print(anime_1.read())
print(anime_1)

class Film(Manga):
    def __init__(self,title,year, genr):
        super().__init__(title,year,genr)
    def __str__(self):
        return super(Film, self).__str__()

film1 = Film(title='Naruto shipyden', year=2012, genr="fantasy")
print(film1)
print(film1.read())