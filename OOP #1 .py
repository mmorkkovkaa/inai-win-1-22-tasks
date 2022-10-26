                                              #АБСТРАКЦИЯ И НАСЛЕДИЕ
# class Car:
#     def __init__(self, title, marka, volume):
#         self.title = title
#         self.marka= marka
#         self.volume = volume
#
#     def __str__(self):
#         return f'title - {self.title}\n'\
#                f'marka- {self.marka}\n'\
#                f'volume - {self.volume}\n'\
#
# usual_car = Car(title="Vaz", marka="Lada", volume= 5)
# print(usual_car)
# print("="*20)
#
# class EuropeAuto(Car):
#     def __init__(self,title,marka,volume,fbs,airbag,esp):
#         super(EuropeAuto, self).__init__(title,marka,volume)
#         self.fbs = fbs
#         self.airbag = airbag
#         self.esp = esp
#
#     def __str__(self):
#         return super(EuropeAuto, self).__str__()+ f'\n abs - {self.fbs}\n'\
#                                                   f'airbag - {self.airbag}\n'\
#                                                   f'esp - {self.esp}'

                                                      #ИНКАПСУЛЯЦИЯ
# class Acaunt:
#     def __init__(self,login, pasword, secret_key):
#         self.login = login
#         self.pasword = pasword
#         self.secret_key = secret_key
#
#     def __str__(self):
#         return f'login - {self.login}\n'\
#             f'pasword - {self.pasword}\n'\
#             f'secret_key-{self.secret_key}'
#
# acc1 = Acaunt(login="Ksenia", pasword= 345612, secret_key="ks345kd234#@!")
# print(acc1)
                                                        # ПОЛИМОРФИЗМ
# class English:
#     def __init__(self,language):
#         self.language = language
#
#     def greeting(self):
#         return f'This person say {self.language} '
#
# class Germany:
#     def __init__(self,language):
#         self.language = language
#
#     def greeting(self):
#         return f'Das mann spriht auf  {self.language} '
#
# class Russian:
#     def __init__(self,language):
#         self.language = language
#
#     def greeting(self):
#         return f'Этот человек говорит {self.language} '
#
# english = English("Good morning!")
# germany = Germany("Guten Morgen!")
# russian = Russian("Доброе утро!")
#
# print(english.greeting())
# print(germany.greeting())
# print(russian.greeting())

