print("=========NUMBER=======")
# in JAVA veriable is a name storage location!
# JAVA vs S languechlarida malumot manzilini nomlanishi
# in Python,veriable is named referanse!
# pythonda hamma narsa object ,/veriable reference ni nomlanishi xolos

count = 100
count_type = type(count)
# print("count:", count, count_type
# format string codlarni qisqartirib bir qator qilib beradi
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator   # state
print(result1, result2)


print("========= String ========")
# METHODS: upper() lower() title() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"the result (1): {result}")


result = course.title()
print(f"the result (2): {result}")

result = course.upper()  # kotta harf bn yozadi
print(f"the result (3): {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")


print("========= boolean ========")
# function > type() input()  boll() int() str()
y = input("Give your value for y: ")  # qiymatni kiriting
print("y:", y)

result = y.isnumeric()
print(f"the input vale is numeric: {result}")


# TRUTHY vs FALSY value lari
# TRUTHY > True
# TRUTHY qiymatlar bu true, hamda sonlar 0 dan tashqari, stringlar TRUTHY qiymatlarni tashkil etdi
test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))


# FALSY > FALSE
# FALSY qiymatilari False ni uzi 0 qiymat, bosh string(""), None lar FALSY qiymatlarni tashkil etdi

# shu yerda 100ni truthy qiymatlaridan birini kirtsak true boladi
test_falsy = "" or False or None or 0
print("test_falsy", bool(test_falsy))  # The FALSY: False
