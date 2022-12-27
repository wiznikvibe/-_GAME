import random
from art import logo, vs
from game_data import data

# How to format account data into printable form
def format_data(account):
    """Takes the account data converts to printable form"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if user is correct."""
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'

print("Welcome to Game of /\ | \/.")
print(logo)
score = 0
game_should_continue = True

# Making account position B become the next account at position A   
account_b = random.choice(data)

# Make game repeatable 
while game_should_continue:
# Generate random account from game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)



    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against Compare B: {format_data(account_b)}")


# Ask User to guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Give user feedback
    # Score Keeping.
    if is_correct:
        score += 1
        print(f"You are right! current Score: {score}")
    else:
        game_should_continue = False
        print(f"You are wrong! final Score: {score}")
    

 