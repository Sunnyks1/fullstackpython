# class student: #class name
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student('penga',88) #s1 is object 
# print(s1.name)
# s1.study() #study is a method


# class student:
#     def details(self):
#         print("had")
# s1=student()
# s1.details()

# student.details(s1)

# ###construct 

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student('penga',88)
# s2=student('denga',31)
# print(s1.name,s1.age,s2.name,s2.age)
# #

# class bank:
#     def __init__(self,balance):
#         self.balance=balance
        
#     def check_balance(self):
#         print("balance is:",self.balance)
# account=bank(1000)
# account.check_balance()



# class user:
#     def __init__(self,name):
#         self.name=name
#     def login(self):
#         print("logged in",self.name)
        
# u1=user('penga')
# u2=user('denga')
# u1.login()
# u2.login()

#######multilevel inheritance
# class grandfather:
#     def house(self):
#         print("house is big")
# class father(grandfather):
#     def car(self):
#         print("car is small")
# class son(father):
#     def bike(self):
#         print("bike is small")
# s=son()
# s.house()
# s.car()
# s.bike()

###########mutiple inheritance
# class father:
#     def house(self):
#         print("father's house")
# class mother:
#     def car(self):
#         print("mother's car")
# class son(father,mother):
#     def bike(self):
#         print("son's bike")
# s=son()
# s.house()
# s.car()
# s.bike()


######heirarchical inheritance

# class father:
#     def house(self):
#         print("father's house")
# class son(father):
#     def bike(self):
#         print("son's bike")
# class daughter(father):
#     def car(self):
#         print("daughter's car")
# s=son()
# s.house()
# s.bike()
# d=daughter()
# d.house()
# d.car()

############str()##########
######used for readable representation of object #######

class student:
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return self.name
    
s1=student('penga')
print(s1)
