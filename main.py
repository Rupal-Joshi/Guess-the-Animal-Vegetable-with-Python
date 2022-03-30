print("would you like to guess an animal of vegetable?")
choice=input("Please choose animal of vegetable? ").lower()
if choice== "animal":
  print("Pick either Ostrich, Lion or Whale")
  print("I will attempt to guess your choice")
  print("Does the animal live in the water? Y/N")
  answer = input().lower()
  if answer == "n": 
    print("Does the animal have wings? Y/N") 
    answer = input().lower() 
    if answer == "y":
      print("It must be an Ostrich!")
    else:
      print("It must be a Lion!")
  else: 
    print("is the animal a mammal?")
    answer=input().lower() 
    if answer=="y": 
        print("it must be a whale")
    else:
        print("It must be a fish")
          
#GUESS THE VEGETABLE
else:
  print("guess the vegetable")
  print("Pick either Carrot, Broccoli, Peas or Sweetcorn")
  print("I will attempt to guess your choice")
  print("Is the vegetable green? Y/N")
  answer = input().lower()
  if answer=="n":
    print("is the vegetable orange? Y/N")
    answer=input().lower()
    if answer=="y":
      print("It must be a carrot")
    else:
      print("It must be sweetcorn!")
  else:
    print("does the vegetable look like a tree? Y/N")
    answer=input().lower()
    if answer=="n":
      print("it must be peas")
    else:
      print("It must be broccoli!")
