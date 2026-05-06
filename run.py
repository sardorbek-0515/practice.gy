# Dunder __builtins__, __init__
# Objectlar ozing bir qator propertylariga (method,state) ega bolgan maxsus datadabe
# PYTHONDA hamma narsa object number, string,"boolean-bool(true, false)"
# int -> butun son
# float -> kasr son (3.14)
# str -> matn
# bool ->ture vs false

message = "Python: HAR DOIM OBJECT!"
print(message)

result = type(message)
print("result:", result)

'''In Python, there are builtin tools:
(1)TYPES > init float str list dict
(2)FUNCTION > print() len() input() type() str() init()
(3)CONSTANTS > Tru False None
'''

print(dir(__builtins__))
