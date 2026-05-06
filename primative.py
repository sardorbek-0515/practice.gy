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
