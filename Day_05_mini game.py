print("Number guessing game")
print("_"*40)
name = input("Enter your name: ")
import random
secrate = random.randint(1,100)
guess = int(input("Guese the number between (1,100): "))
attempt = 1
while guess != secrate:
  if guess > secrate:
    print("Too high")
  else :
    print("To low")
  guess = int(input("Guess the number "))
  attempt = attempt + 1
if guess == secrate:
  print("Congratulation",name,"You Win !")
  print("You Guesed the number in",attempt,"Attempts")
