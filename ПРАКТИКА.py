class JunDev:
    def __init__(self, name, age, language ):
         self.name = name
         self.age = age
         self.language = language


    def __str__(self):
         return f'Имя - {self.name}\n'\
                f'Возраст- {self.age}\n' \
                f'Язык.прог- {self.language}\n'



    def education(self,stude_placce ):
        if stude_placce == "Школа":
            return f'Вам стоит записаться на курсы'
        elif stude_placce == "Курсы программирования":
            return f'Отличная база!'
        else:
            return f'Тоже пойдёт!'

    def work(self, company):
        if company == "Google":
            return  f'О, да вы из {company}! Богатые родители или просто умный? '
        elif company == "Местная компания":
            return f'O,это {company}! Неплохое начало!'
        else:
            return f'Быть безработным не стыдно!'


worker1 = JunDev("Пётр", 17,"Python")
print(worker1)
print(worker1.work(str(input("Где вы работаете?"))))
print(worker1.education(str(input("Где вы проходили обучение?"))))

class MidDev(JunDev):
    def __init__(self,name, age, language,country, stage,recomendation):
        super(MidDev, self).__init__(name, age, language)
        self.country = country
        self.stage = stage
        self.reromendation = recomendation

    def __str__(self):
        return super(MidDev, self).__str__()+f'{self.country}\n' \
                                              f'{self.stage}\n'\
                                                f'{self.reromendation}\n'\

    def job(self,vocation):
        if vocation == "Бэкенд":
            return f'Вы специализируетесь на {vocation}? Вам к нам!'
        else:
            return f'Вы нам не подходите!'

worker2 = MidDev("Алиса", 23,"Python", "Англиля", "5 лет","Есть")
print("-"*20)
print(worker2)
print(worker2.job(str(input("Кем вы бы хотели у нас работать?"))))

class SenDev(MidDev):
    def __init__(self,name, age, language,country, stage,recomendation,workplace,eye_color,sername):
        super(SenDev, self).__init__(name, age, language,country, stage,recomendation)
        self.workplace = workplace
        self.eye_color = eye_color
        self.sername = sername

    def __str__(self):
        return super(SenDev, self).__str__()+f'{self.workplace}\n' \
                                              f'{self.eye_color}\n'\
                                                f'{self.sername}\n'\


    def money(self,salary):
        if salary <= 3500:
            return f'Вы хотите получать {salary} за работу? Вам к нам!'
        elif salary >= 3500:
            return f'А вы не обнаглели?'
        else:
            return f'Нормально отвечайте ёмаё!'


worker3 = SenDev("Эдуард", 34 ,"Java", "Цвикау", "10 лет","Есть","Google company","Зелёный","Альбертович" )
print("-"*20)
print(worker3)
print(worker3.money(int(input("Сколько вы хотите зарабатывать?"))))



