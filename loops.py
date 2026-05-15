'''   LOOP operators
      (1) for   #{ketmaketlik aniq boladi}
      (2) break/else
      (3)while #shartga qarab ishlaydi
'''
print("========== (1) for operator============")  # {ketmaketlik aniq boladi}
# For - belgilangan tartibda, belgilangan ketmaketlikda ishga tushishi nazarda ttilgan mantiqlar uchun ishlatiladi
# Iterable object > string dict tuple list range map filter / takrorlanish xususiyatga ega object
text = "MIT"  # 3maarta loop boladi
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferarri", year=2025)  # 2marta taakrorlanadi
range_obj = range(5)  # [0, 5]

for letter in text:  # loop qilib beradi
    print(f"the letter: {letter}")

print("------")

for number in numbs:
    print(f"the number: {number}")

print("----------")
for x in range_obj:
    print(f"the element: {x}")

print("----keylarni qolga kiritsh---")
for key in car_obj:  # brend / year
    print(f"the key: {key}")


print("----keylar & value qolga kiritsh---")
for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

print("----------")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    # ➡️ range(1, 20, 5) = 1 dan boshla, 20 ga yetguncha, har safar 5 ga oshir


print("========== (2) break/else ============")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("Tanafusga chiqdik")
        break  # break majburiy toxtatish
else:                # break bolmasa else amalga oshadi
    print("Lopp amali hech qanday xatoliksz amalga oshdi ")


print("==========  (3) while  operator =========")
# ketmaketlik noaniq boladi shartga qarab ishlaydi
numb = 40
while numb > 0:  # shart
    numb -= 10  # har ishga tushganda 10ga kamayadi
    print(f"raqam teng {numb}")

print("----------")
count = 0
while True:
    count += 1
    x = int(input("Raqamni toping"))  # ketmaketlik noaniq boladi

    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print("Wrong, please find again")
