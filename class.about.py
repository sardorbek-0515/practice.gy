''' CLASS
    (1) What is class
    (2) ordinary vs static properties
    (3)special method
    
'''

print("================ CLASS uzi nima  ==================")
# CLASS lar objct yasash uchun xizmat qiladigan shablon hissoblamnadi
# class - blueprint for object creation !
# static sozini korish bn obj bn emas classni uzi bn keladigan propertylar hisoblanadi


class Person():  # 3ta structurasi bor
    # state
    message = "static class state propert"

    # constructor
    def __init__(self, name, age):  # self bu object
        self.name = name
        self.age = age
        pass

    # method   # harakati  /classni objctlari
    def introduce(self):
        print(f"{self. name} says: How do you do!")

    def say_age(self):
        print(f"{self. name} says I am {self.age} ")
       # static/class method

    @classmethod
    def explain(cls):
        print("static method propert execed!")


person1 = Person("Jack", 24)
person2 = Person("Martin", 35)
person3 = Person("John", 27)

# ordinary state property / odatiy state prpertylari
name = person1.name
print("person1.name:", person1.name)

# ordinary method state / odatiy state propertylar
person1. introduce()
person2.say_age()

print("================ ordinary vs static properties  ==================")
# Static state ishlatganda togridan togri objct bn emas classni uzi bn keladigan statelar message
new_massage = Person.message
print("new_message:", new_massage)


# static method /ishg TUSHIRISH
Person.explain()
