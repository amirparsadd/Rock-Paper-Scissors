import random as rng
import os
import time

results = {
    "rp": True,
    "rs": False,
    "sp": False
}

names = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

def clear():
    # check and make call for specific operating system
    os.system('clear' if os.name == 'posix' else 'cls')

def validate_input(a) -> bool:
    if(len(a) != 1): return False
    return ["r", "p", "s"].__contains__(a)

def main():
    enemy_points = 0
    user_points = 0

    while True:
        enemy_choice = list(names.keys())[rng.randint(0,2)]
        user_choice = "blyat davai"
        while validate_input(user_choice) == False:
            user_choice = input("Enter Your Attack (rps): ")
        
        print(f"You Chose {names[user_choice]}")
        time.sleep(0.5)
        print(f"Your Enemy Chose {names[enemy_choice]}")

        if(enemy_choice == user_choice):
            print("Its A Tie!")
            clear()
            continue
        
        result = None
        if(list(names.keys()).__contains__(user_choice + enemy_choice)):
            result = results[user_choice + enemy_choice]
        else:
            result = not results[enemy_choice + user_choice]
        
        print("You Lost" if result else "You Won!")

if(__name__ == "__main__"):
    main()