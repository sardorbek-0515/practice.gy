''' Comprehnnsion
    (1) What is comprehension & list comp.
    (2) Set anad dictionary comp
'''

print("=============== (1) What is comprehension & list comp.=================")
# Comprehension acts like spread operator! /spred operatorni pythonda taqdim etadi
# /Comprehension tarqalish operatori kabi ishlaydi!
''' 
    Comprehnnsion general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c)<expression> for item in iterable <condition>

'''

# list comp
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("--------")
people = [("Robert", 20), ("Leo", 18), ("Jack", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)


cars = [
    ("Ferrari", 78),
    ("Tayoto", 87),
    ("Audi", 110),
    ("BWM", 109),
    ("Pagani", 33)
]
list_car = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_car)

print("============  (2) Set anad dictionary comp=========")
numbs = [1, 5, 4, 20, 1, 20, 4, 5]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

dict_people = {person[0]: person[1] for person in people}  # b version
print("dict_people:", dict_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1 > 20]}  # c version
print("dict_people2:", dict_people2)
# (<expression> for item in iterable) generic
