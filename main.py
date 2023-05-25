import random
from art import logo, vs
from game_data import data
from replit import clear

def display_account(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description} from {country}"

def checker(answer, a_followers, b_followers):
    # Check guess against the follower account
    if a_followers > b_followers:
        return answer == "a"
    else:
        return answer == "b"

print(logo)
score = 0
continue_game = True
accountB = random.choice(data)

while continue_game:
    # Pick a random instagram account
    accountA = accountB
    accountB = random.choice(data)
    
    while accountA == accountB:
        accountB = random.choice(data)
    
    print(f"Compare A: {display_account(accountA)}.")
    print(vs)
    print(f"Against B: {display_account(accountB)}.")
    
    answer = input("Who has more followers? 'a' or 'b'': ").lower()
    a_followers = accountA["follower_count"]
    b_followers = accountB["follower_count"]
    correct = checker(answer, a_followers, b_followers)
    clear()
    print(logo)
    if correct:
        score += 1
        print(f"Correct! Current score: {score}\n")
        
    else:
        print(f"Wrong! Streak: {score}\n")
        continue_game = False
