import random
guessNumber=int (input("Enter the Guess Number 1 to 100:"))
randomNumber=random.randint(1,100);
while guessNumber!=randomNumber:
    guessNumber=int (input("Enter the Guess Number 1 to 100:"))
    if guessNumber<randomNumber:
        print("Guess Number is higher",randomNumber)
    elif guessNumber<randomNumber:
        print("guess Number is logger",randomNumber)
    else:
        print("You win!")



