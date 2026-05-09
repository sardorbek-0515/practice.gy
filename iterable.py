print("========  Iterable object & Range  ======================")
# Iterable object > string dict tuple list range map filter

# text = "Mit"  # text veriable hosil qilib mitga teglash
# for letter in text:
#     print(f"the letter:{letter}")

range_obj = range(3)  # bunda (0, 3 gacha lekn 3 x hisoblanmaydi)
print("range_obj:", range_obj)

for letter in "Mit":
    print(f"the letter:{letter}")
for ele in range_obj:  # itereble qilish mumkin 0,1,2 singari
    print(f"the element: {ele}")  # ele 0,1,2qilib beradi


print("===========   DICTIONARY ======================")
# DICTIONARY lar JSON object ham  deb ataladi, mahsus method yani None emas error chiqadi
# DICTIONARY bu itereble objectlardan hissoblanadi
person = {"name": "JACK", "age": 25, "single": True}
person_obj = dict(name="JACK", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")
# 1- yoli shu dictionaryni ichidagilardan foydalanib
name = person_obj["name"]
print("name:", name)

age = person_obj["age"]
print("age:", age)

# 2- method: get()  /bunda build methodi get hamda dectionart bn qolga olsa boladi va bunda mavjud bolmagan qiymatlarni None qabul qiladi
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

# dic intrable ligiga misol: person_obj dagi hamma qiymatlarni olib beradi olib beradi
# for key in person_obj:
#     print(f"the key: {key}")

# Agar biz birorta person_obt ichidan birostasini ochirmoqchi bolsak
# del person_obj["single"]
# for key in person_obj:
#     print(f"the key: {key}")

# Agar biz key hamda valuesini olmoqchi bolsak
for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]}")
    # print(f"the key: {key} > value {person_obj.get(key)}") # bu holatda get orqali qilsak ham boladi
