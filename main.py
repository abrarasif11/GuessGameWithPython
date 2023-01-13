from random import randint

for x in range(10,16):
  guessnumber = int(input("Enter Your Guess Number Between 10 to 16 : "))
  randomNumber = randint(10,15)

  if guessnumber == randomNumber:
    print("Congo! You Won...")
  else:
    print("Sad! You Lost!!!")
    print("Random number was : ",randomNumber)