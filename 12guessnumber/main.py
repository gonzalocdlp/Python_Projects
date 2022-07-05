import random
game_start="y"
while game_start=="y":
    print('Welcome to number guesser')
    difficulty=input('Choose your difficulty easy or hard. Type 1 for easy and 2 for hard')
    difficulty=int(difficulty)
    #get random number
    random_number=random.randint(1,100)
    guesses=15
    if difficulty==1:
        print('You have 10 guesses to solve')
        guesses=10
        og=11

    if difficulty==2:
        print('You have 5 guesses to solve')
        guesses=5
        og=6 #to announce trial number

    while guesses > 0:
        guess=input(f'type in your guess number {og-guesses}\n')
        guess=int(guess)
        if guess==random_number:
            print('you won congrats')
            #restart
            game_start=input("Play again? Input 'y' to restart. Otherwise, input any other key")
            if game_start=="y":
                print("restarting..")
            else:
                print('goodbye')
        if guess>random_number:
            guesses=guesses-1
            print(f'too high. You have {guesses} left')
            
        if guess<random_number:
            guesses=guesses-1
            print(f'too low. You have {guesses} left')
            
    print("you lost no more guesses")
    game_start=input("Play again? Input 'y' to restart. Otherwise, input any other key")
    if game_start=="y":
        print("restarting..")
    else:
        print('goodbye')