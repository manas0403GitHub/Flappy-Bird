import random
import os

# Generate a random number between -50 and 50 for the initial pipe height
pipeHeight = random.randint(0, 50)

# Initialize variables
flap = 0
move = 0
score = 0

os.system('cls' if os.name == 'nt' else 'clear')

def game_loop():

    global pipeHeight
    global score
    global move
    global flap

    print("Flappy Bird!🐦")
    menu = input("""S(Start)▶️,
Q(Quit)❌:""")
    

    if menu == "S":
        while True:
        
            print("Score: ", score)
            # Prompt the user to flap or fall
            flapOrNot = input("Flap (Fl) or Fall (Fa)?> ")

            # If the user chooses to fall
            if flapOrNot == "Fa":
                print("Continue falling...")
                flap -= 10
                move += 1
                continue

            # If the user chooses to flap
            elif flapOrNot == "Fl":
                print("Flap!")
                flap += 10
                move += 1

            
            # If the pipe height is 0, generate a new random height
            if pipeHeight == 0:
                pipeHeight = random.randint(-50, 50)
                continue

            # Check if the player touched the pipe
            if pipeHeight <= flap:
                print("You touched the pipe, Game over!")
                playAgain = input("Again (Y(Yes) / N(No))?> ")

                # If the player wants to play again
                if playAgain == "Y":
                    pipeHeight = random.randint(-50, 50)
                    flap = 0
                    move = 0
                    continue

                # If the player doesn't want to play again
                elif playAgain == "N":
                    exit()

            # Check if the player passed a pipe
            elif not pipeHeight == flap and move == 6:
                print("You passed a pipe, 1 point added!")
                score += 1
                move = 0
                continue
            os.system('cls' if os.name == 'nt' else 'clear')

    elif menu == "Q":
        exit()

game_loop()