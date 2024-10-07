import random
act_num = random.randint(1,100)

while True:
    try:
        guessed_num = int(input("\nGuess the number between 1 and 100 : "))
        
        if guessed_num < act_num:
            print("Too low!")

        elif guessed_num > act_num:
            print("Too High!")
        
        else:
            print("Congractulations! You guessed a correct number\n")
            break
    except ValueError:
        print("Plaease enter a valid number")