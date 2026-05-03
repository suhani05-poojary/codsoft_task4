import random

def get_computer_choice():
    return random.choice(["rock","paper","Scissors"])

def decide_winner(user,computer):
    if user==computer:
        return "tie"
    if(user=="rock" and computer=="scissors") or \
    (user=="paper" and computer=="rock") or \
    (user=="scissors" and computer=="paper"):
        return "user"
    return "computer" 

def main():
    user_score=0
    computer_score=0
    print("\n=== Rock Paper Scissors Game ===") 
    while True:
        user=input("\nEnter rock/paper/scissors : ").lower()
        if user not in ["rock","paper","scissors"]:
            print("Invalid input.Try again.")
            continue
        computer=get_computer_choice()
        print("You chose:",user) 
        print("Computer chose:",computer) 
        result=decide_winner(user,computer)
        if result=="tie":
            print("It's a tie!")
        elif result=="user":
            print("You win!")
            user_score+=1
        else:
            print("Computer wins!")
            computer_score+=1
        print(f"Score-> You:{user_score} | Computer:{computer_score}")
        play_again=input("Play again?(Yes/No): ").lower()
        if play_again!="yes":
            print("Game ended.")
            break

if __name__ =="__main__":
    main()                                    