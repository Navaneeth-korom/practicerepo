import random

def rock_paper_scissors():
    choices = ["r","p","s"]
    choice_map ={'r': 'Rock', 
                'p': 'Paper',
                's': 'Scissors'}
    while True:
        start = input("PLAY ROCK, PAPER, SCISSORS ? (y/n): ").lower()
        if start == 'y':
            your_score = 0
            computer_score = 0
            draw = 0
            round_num = 1
            while True:
                print(f"---------- Round {round_num} ----------")
                user_choice = input("Rock, paper, scissors ? (r/p/s): ").strip().lower()
                if user_choice == "r" or user_choice == "p" or user_choice == "s":
                    computer_choice = random.choice(choices)
                    print(f"Your choice = {choice_map[user_choice]}")
                    print(f"Computer choice = {choice_map[computer_choice]}")
                    if computer_choice == user_choice:
                        print("Draw")
                        draw += 1
                    elif (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r")or (user_choice == "s" and computer_choice == "p"):
                        print("You won")
                        your_score += 1
                    else:
                        print("You lose")
                        computer_score += 1
                else:
                    print("Invalid choice!")
                play_again = input("Play again? (press y). press any other key to exit: ").strip().lower()
                if play_again == 'y':
                    round_num += 1
                    continue
                else:
                    break
            print(f"\nThe final score is")
            print(f"Total rounds played = {round_num}")
            print(f"Your score          = {your_score}")
            print(f"Computer score      = {computer_score}")
            print(f"No.of Draw games    = {draw}")
            if your_score > computer_score:
                print("You won the game")
            elif your_score == computer_score:
                print("Game Draw")
            else:
                print("You lost the game")
            break
        elif start == 'n':
            print("Thank you")
            break
        else:
            print("Invalid choice")

rock_paper_scissors()
    