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
