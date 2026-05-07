'''FUNCTIONS
(1) DEFINE VS CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("============= DEFINE (parametr) vs CALL (argument)==============")
# build in function > print() type()
# Function - malum bir joyda malum bir mantiqni ishga tushirib beruvchi code block!
# Instead of block {} in JAVA, Python uses indentation!        /"JAVA’da {} bloklari o‘rniga, Python’da bo‘shliq (indentatsiya) ishlatiladi!"

# JS da funtionlarni qiymat qaytarish boyicha 2 xil kreteriasi bor   return vs void
# return- function ichida qiymat qaytaradi, Natijani saqlaydi, Hissob kitob bajarari
# void - qimat qaytarmaydi JSda function qiymat qaytarmasa avtomatic (undefined) qaytaradi || LEIKN PYTHON da uning orniga (None)qaytaradi, ish bajaradi qiymat qaytarmaydi!
# return > natija ber,   Natijani saqlaydi, Hissob kitob bajaradi
# void >  faqat bajar,   ish bajaradi qiymat qaytarmaydi!


# DEFINE -build  functionni-qurish, [a] Parametr
# Bu funksiya parametr sifatida a qabul qiladi va uni  print orqali ekranga chiqaradi:
def greet(a):     # greet() faqat ekranga chiqaradi,
    # pass           # bosh qoldirib bolmas ekan pass  qoyish kerak hech narsa mavjud emas hech narsa qilama degani
    print(f"How do you do, {a}")


def greeting(b):  # greeting() esa qiymat qaytaradi.
    print("greeeting is executed")  # bunda birinchi chiqadi kn
    return f"Hi {b}"  # kn return orqali qiymat qaytaradi

  # Call - execute -chaqirish
natija1 = greet('Jack')  # void function
print("natija1:",  natija1)
# How do you do, Jack
# natija1: None


natija2 = greeting('Jastin')  # return function
print("natija2:", natija2)
# greeeting is executed
# natija2: Hi Jastin


print("=============  Keyword & default arguments  ==============")


# DEFINE
def give_greet(name, age=28):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
# biz shu yerda  Keyword dan foydalanishmiz mumkin boladi "Jack",24 bu holatda bir xil ishlaydi farqi bizni codemizni korgan odam yaxshi tushunadi
natija3 = give_greet(name="Jack", age=24)
print("natija3:", natija3)

# DEFAULT argument
# bu yerda age=28yoshni yozmasak default holatda tepadan oladi
natija4 = give_greet("John")
print("natija4:", natija4)


print("============= Scope  ==============")
b = 100  # 3 tashqaridan izlaydi


# DEFINE
def calculate(a):  # 2 prametr tashqaridan izlaydi
    c = a * b  # 1 ichkaridan izlaydi
    print(f"the c value: {c}")  # format string

    # Call
calculate(5)
