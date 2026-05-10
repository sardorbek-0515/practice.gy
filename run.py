# Dunder __builtins__, __init__ - bu megic    pythoni ichki qurilish mehanizmi

# Maxsus methodlar Dunderlar orqali belgilanadi Pythoni uzini ichki sistem verblar builtins dunderi orqali qabil qilingan
message = "Python: HAR DOIM OBJECT!"
print(message)

result = type(message)
print("result:", result)

# Turli tuman komandalar mujassam
'''In Python, there are builtin tools:
(1)TYPES > init float str list dict
(2)FUNCTION > print() len() input() type() str() init()
(3)CONSTANTS > Tru False None
'''

print(dir(__builtins__))  # Turli tuman komandalar mujassam
