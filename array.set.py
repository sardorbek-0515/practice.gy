''' Array & Set 
    (1) Array
    (2) Set
    (3) Specific operators with set
'''

from array import array
print("=====================  (1) Array ================================")

# Bu arraylarni ota masusu xollarda ishlatiladi,katta hajm sonlar un
numbers = array("i", (1, 4, 5, 7, 8, 41))  # katta hajm sonlar un
print("numbers(1):", numbers)

# method

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(2):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)
