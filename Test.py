# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# ch = thislist[2]
# print(ch[2])jk = 8

#
# def recurse(jk):
#     if jk > 3:
#         result = jk + recurse(jk-1)
#         print(result)
#     else:
#         result = "Ended"
#     return result
#     print(result)
#
#
# recurse(2)

# x = lambda a: a
#
# print(x(1))

# x = ["Kia", "volvo", "Honda", "Skoda", "Benz", "BMW", "Toyota", "Hyundai"]
# x.insert(6, "Ford")
#
# i = x.index("Honda")
# y = x[int(i * 2)]
# print(x)
#
# class Car:
#     def __init__(self, model , year):
#         self.model = model
#         self.year = year
#
#     def caller(self):
#         print(self.model, self.year)
#
#
# car = Car("Camry", 2008)
# car.caller()
#
# class Toyota(Car):
#     def __init__(self, model, year, color):
#         Car.__init__(self, model, year)
#         self.color = color
#
#
#     def paint(self):
#         print("My car is a",self.model, self.year, "and i'd like to paint it", self.color)
#
#
# car = Toyota("Camry", 2008, "Gold")
# car.paint()

# x = 300

# def variable():
#     y = global x
#     x = 200
#     print(x)
#
# variable()
#
# print(x)

# city = input("What City did you grow up in? \n")
# pet = input("What is the name of your pet? \n")
#
# print("Your bandname could be", city, pet)
# tookool234723A

# print("Welcome to the tip calculator \n")
# bill = input("What was the total bill? $")
# percentage = input("What percentage tip would you like to give? 10, 12 or 15: ")
# number = input("How many people to split the bill? ")
#
# pay = ((int(percentage)/100) * int(bill)) + int(bill)
#
# final_bill = int(pay) / int(number)
#
# txt = "Each person should pay: ${:.2f}"
#
# print(txt.format(final_bill))

num = input("What number would you want to choose?: ")

if (int(num) % 2) == 0:
    print("Your number is even")
else:
    print("Your number is odd")
