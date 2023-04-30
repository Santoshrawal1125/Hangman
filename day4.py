import random

user=int(input("enter 1 for rock 2 for paper and 3 for scissor"))

random_number=random.randint(1,3)
print("computer choosed ",random_number)

if(user==1 and random_number==2):
  print("computer chooses paper you lost")
elif(user==2 and random_number==3):
  print("computer chooses scissor you lost")
elif(user==3 and random_number==1):
  print("computer chooses rock you lost")
elif(user==random_number):
  print("Draw")
else:
  print("you win ")
