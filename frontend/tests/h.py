# for i in range (0, 10):
#     if i % 2 == 0:
#         print(f'{pow(i, 3):.1f}')
#
#
# def calcx(num: float) -> float:
#     if num <=1:
#         return 1
#     else:
#         return num * calcx(num -1)
# print(f"The calx output of 4 is: {calcx(4)}")
#
# from re import compile, sub, IGNORECASE
#
# pattern = compile("[^A-Z]+", IGNORECASE)
# string = sub(pattern, "", "A man, a plan, a canal, Panama!")
# print(f"Output is: {string}")

# print(5//2)
#
# print("Enter username: ")
# try:
#     username = input("")
#     if username =="admin":
#         print("Superuser...")
#     else:
#         print("Regular user...")
# except IOError as err:
#     print(err)

# data: int = [1, 2, 3, 1, 2, 3, 4, 4, 4, 5, 6, 9, 1, 1, 2]
#
# set_data = set()
#
# try:
#     for i in data:
#         set_data.add(i)
#         print(set_data)
# except TypeError as err:
#     print(err)

# myVar: int = 42
# str_formatted: str = f"myVar contains {myVar:f}"
# print(str_formatted)

# emails = []
#
# emails.append("huck.finn@qa.com");
# emails.append("robin.loxley@qa.com");
# emails.append("claire.jones@qa.co.uk");
#
# emails = []
#
# print(f"List is {emails}")


# areas = dict()
# areas["01242"] = "Cheltenham"
# areas["01453"] = "Stroud"
# areas["01452"] = "Gloucester"
# areas["01793"] = "Swindon"
#
# print(areas)

#
# class Test:
#     def __init__(self):
#         self.__code = 99
#
#     def show(self):
#         print("Test class!")
#
#     def get_code(self):
#         return self.__code
#
# mytest = Test()
# print(mytest.get_code())
# print(mytest.__code())
# mytest.show()
#
#
#
# class BankAccount:
#     def __init__(self, acc, startbal):
#         self.__accnum = acc
#         self.__balance = startbal
#         print("Account created")
#
# class StudentAccount(BankAccount):
#     def __init__(self, acc, startbal, od):
#         super().__init__(acc, startbal)
#         self.__overdraft = od
#
# student1 = StudentAccount("12345678", 100.0, 500.0)

#
# data = [33, 113, 41, 112, 34, 10, 9, 27, 35]
#
# XXX = datum in data
# YYY = datum > 10 and datum < 35
# ZZZ = datum % 2 == 1
#
# for XXX:
#     if YYY:
#         if ZZZ:
#             print(datum)
#
# not an interger
#
# data = [i for i in range(1,6)]
#
# data = [1, 2, 3, 4, 5]
#
# data = list(range(1,6))
#
# data = range(1,6)

str1 = "The cat sat on the mat. My cat is called Frank. Cats are cute!"
wh = str1.replace("cat", "dog").upper().index("dog")
print(wh)