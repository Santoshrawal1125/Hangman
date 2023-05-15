import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |       
      |       
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



word_list=["aeroplane","mobile","engineer"]

chosen_word=random.choice(word_list)

# print(f"the word is {chosen_word}")

display=[]
for _ in range(len(chosen_word)):
  display+="_"
print(display)
i=1
lives=6
n=1




while(i<=len(chosen_word)):
  guess=input("Enter a letter to guess the word :\n").lower()
  
  for postion in range(len(chosen_word)):
    letter = chosen_word[postion]
    
    if letter==guess:
     display[postion]=letter
  print(display)
  
  if guess not in chosen_word:
    lives-=1
    
    if lives==0:
      print(stages[0])
      print("you lose the game") 
      break
  print(f"{' '.join(display)}")
  
      
  
  if "_" not in display:
    print("you won the game")
    break
  i=i+1
  print(stages[lives])
