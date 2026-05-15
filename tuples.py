''' Tuple
    (1) What is tuple: typle vs list
    (2) Unpacking arguments
    (3)zip
'''

print("========= (1) What is tuple: typle vs list =======")
# Java/PHP/NodeJS array => Python list
# LIST 2 XIL USULDA QURILADI

# literal
numbs = [3, 5, 1, 2]


# constructor / hamma constructor function korinishda boladi
letters = list("Hello World")

fruits = ["Apple", "Lemmon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"  # ozgartirish
print("after fruits:", fruits)


# Tuple -ichidagi qiymatni ozgarishga yol qoymaydi /bir marta qiymat beriladi
animals = ("dog", "cat", "fish," "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "brid" # Tuple ligi un ozgarmaydi

# try avoid thse
people = "Andrew", "John"
animals = "dog",

print("==== (2) Unpacking arguments =====")
groups = ["MIT", "FLEX", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print(" *args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# call
calculate(1, 7, 2, 3)
calculate(0, 2, 3000)
calculate(5, 7)


print("-------------")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi I am {kwargs["name"]} and I am{kwargs["age"]} year old! ")


# Call
introduce(name="Jastin", age=25)
introduce(name="Shawn", age=25, singler=True)
print("-------------")


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# Call
greeting("hi", True, 10, name="John", age=22)


print("========= (3) ZIP  =======")  # Iterable object zip
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)
resilt = list(zipped)
print(f"the result: {resilt}")
