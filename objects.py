''' Object
    (1) What is object
    (2) Iterable object & RANGE
    (3) DICTIONARY
    (4) Error handing system
'''
# Objectlar ozing bir qator propertylariga (method,state) ega bolgan maxsus datadabe
# PYTHONDA hamma narsa object number, string,"boolean-bool(true, false)"
# int -> butun son  stringni intigerga aylantirib beradi
# float -> kasr son (3.14)
# str -> matn  intigerni stringa aylantirib beradi
# bool ->ture vs false

# packagelar/module
import array  # import  qilish kerag boladi bular python bn yonmayon umr koradi
import math  # import  qilish kerag boladi bular python bn yonmayon umr koradi
from math import ceil  # packegning ichidagi ceil methodini qolga oldik
print("============= What is OBJECT===========")
# An object has state and method properties  // Objlar uzining state hamda method lariga ega maxsus datadaybe
# State- insoni yosh,irq,ism,familya  / bu obctga dahldor bolgan state
# method- harakatlari, yurishi,uqishi,taomlashishi bu obctga dahldor bolgan method
# Everything is object in Python! / pythonda hamma narsa objct

print(type('Hello World!'))  # type function hamda "string"
print(type(100))
print(type(True))
print(type(array))
print(type(math))
# Class bu shablon obectni hosil qilishda ishlatiladigan shablon
# bular hammasi classdan olingan instnlar hissoblanadi va hammasi object hissoblanadi


# Paradign > Function Programming  chiziqli paradigma deb ham ataladi verbl hamda func dan iborat dasturlash hissoblanadi
# & OOP  / obectlarga asoslangan  dasturlash va 4 conceptga ega hamma tilda uchraydi
# OOP 4 CONCEPT > Abstraction | Encapsulation | Inheritence | Polimorphism
result1 = math.ceil(97.7)  # Call
# reslt veriableni meth objctni ceil methodga orgiment sifatida pass qilamiz/asosan nomeric bn ishlaydi
print("result1:", result1)


result2 = ceil(98.7)
print("result2:", result2)


print("================ Error handling system  => xatoni boshqarish tizimi ,tuzatish ===================")
car_dict = dict(name="Tayota", year=2026, electric=True)
# dictionary ichida mavjud bolmagan bir qiymatni(state) qabul qilamiz
#  result = car_dict["origin"]
#     print("result:", result) # Bu holatda error chiqadi origin mamlakat yoq

# errorni handling qilamiz , yani tuzatamiz
# #agar tryni ichidagi mantiq xatolik sodir etsa u except degan bolimga boradi va bu bolimda KeyError hosil bolsa uni err nommi bn belgilatib uning ustida amal qilishga yani tuzatishga harakat qilamiz
try:
    print("shu yerdan otdi")  # try ishga tushganligini bilish un
    result = car_dict["origin"]  # bu yerda kod toxtaydi va(66)qatorga yuboradi
    print("result:", result)
except KeyError as err:   # agar dic ichda bor state bolsa error ishlamaydi
    print("bunday malumot topilmadi:", err)
    # shu mantiqlar hatosiz ishga tushsa else ishga tushadi
else:
    print("Executed successfully without errors")  # hatolik borligi unishlamyd
finally:                                        # oxrg mantiq kk bolsa finally xato bor yoqligiga qaramaydi ishlayveradi
    print("Final closing logic")

    # print(dir(_builtins)) qilsak boshqa errorni ham korsak boladi


print("==============togrisi==========")
try:
    print("shu yerdan otdi")  # try ishga tushganligini bilish un print
    result = car_dict["year"]  # bu yerda kod ishlaydi bor statedan qoshldi
    print("result:", result)
except KeyError as err:   # agar dic ichda bor state bolsa error ishlamaydi
    print("bunday malumot topilmadi:", err)
    # shu mantiqlar xatoszligi un else ishga tushadi
else:
    print("Executed successfully without errors")
finally:                                        # oxrg mantiq kk bolsa finally xato bor yoqligiga qaramaydi ishlayveradi
    print("Final closing logic")


print("============ AttributeError ==============")
# car_dict ning uzida build in bolgan statelaridan ishlatamiz
try:
    print("shu yerdan otdi")  # try ishga tushganligini bilish un
    a = car_dict.speed          # car dic ischda bolmasin qandaydir state
    result = car_dict["origin"]  # bu yerda kod toxtaydi va(66)qatorga yuboradi
    print("result:", result)
except KeyError as err:   # bunday bolsa  error ishlamaydi himoya qilolmayd
    print("bunday malumot topilmadi:", err)
except AttributeError as err:   # agar dic ichda bor state bolsa error ishlamaydi
    print("No speed found:", err)
    # shu mantiqlar hatosiz ishga tushsa else ishga tushadi
else:
    print("Executed successfully without errors")  # hatolik borligi unishlamyd
finally:                                        # oxrg mantiq kk bolsa finally xato bor yoqligiga qaramaydi ishlayveradi
    print("Final closing logic")
