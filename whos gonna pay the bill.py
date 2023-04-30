import random

names=input("give me everybody name seperated by a comma ")

name=names.split(",")

pay=random.choice(name)

print(pay +"is going to pay the bill")

