''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging

'''

import turtle
print("=============  (1) Python Packages & Core Package=============")
''' PYThon Packages/Modules: Core, File and External'''  # jsda package emas Library deyiladi
# Core Packeges > https://docs.python.org/3/library


# Core packages
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)
# turtle.done()

# ochilgan faylni albatta yopish kerak
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with - faylni ozi yopadi
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("SHU yerdan otdi")
