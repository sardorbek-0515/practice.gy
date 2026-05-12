''' CLASS deep diving
    (1) ENCAPSULATION <
    (2) INHERITENCE
    (3) POLIMORPHISH
'''

print("=========== ENCAPSULATION  -himoyalsh=============")
# C++ JAVA > public protected
# PHP TypeScript > public private protected

# ENCAPSULATION > public __private mantiq qurb beradi  _ protect qonuniayti


class Account:
    # state
    description = "Bu klass bank hisoblarini yaratadi"

    # constructor
    def __init__(self, owner, amount):  # private qilindi ximoya qilindi
        self.__owner = owner
        self.__amount = amount

    # metod: balansni ko‘rsatish
    def get_balance(self):
        print(f"Hisob egasi: {self.__owner}, balans: {self.__amount} USD")

    # metod: pul qo‘shish
    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    # metod: pul sarflash
    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

# getter => yani malumotlarni to'g'ridan to'g'ri olib o'qishimiz mumkun

    @property
    def holder(self):
        return self.__owner

# setter => malumotllarni o'zgartirish®
    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Jack", 1000)
my_account .get_balance()


print("------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("----------")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("Siz aytgan state topilmadi:", err)

# account_owner = my_account.holder  # state
# print("account_owner:", account_owner)# mahfiy malumot olish


# => getter vs setter
print("current owner before:", my_account.holder)  # state use
my_account.holder = "Martin"
print("owner after:", my_account.holder)  # state use
