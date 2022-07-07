import game_data as game
import random
import os
import art
#select random first celebrity
amount_names=len(game.data)
rand_celeb=random.randint(0,amount_names-1)
celeb1=game.data[rand_celeb]['name']
celeb1_follower=game.data[rand_celeb]['follower_count']
celeb1_description=game.data[rand_celeb]['description']
celeb1_country=game.data[rand_celeb]['country']
new_game='y'
score=0
#continuous loop
while new_game=='y':
    #select 2nd celebrity
    rand_celeb=random.randint(0,amount_names-1)
    celeb2=game.data[rand_celeb]['name']
    celeb2_follower=game.data[rand_celeb]['follower_count']
    celeb2_description=game.data[rand_celeb]['description']
    celeb2_country=game.data[rand_celeb]['country']
    # so it's not same celebrities
    if celeb2==celeb1:
        rand_celeb=random.randint(0,amount_names-1)
        celeb2=game.data[rand_celeb]['name']
        celeb2_follower=game.data[rand_celeb]['follower_count']
        celeb2_description=game.data[rand_celeb]['description']
        celeb2_country=game.data[rand_celeb]['country']

    print(art.logo)
    print(f'Compare A: {celeb1} a {celeb1_description} from {celeb1_country}')
    print(art.vs)
    print(f'Compare B: {celeb2} a {celeb2_description} from {celeb2_country}')
    answer=input("Who has more followers? Type 'A' or 'B':").lower()
    #determine winner
    if celeb1_follower>celeb2_follower:
        winner='a'
    else:
        winner='b'
    #the winner
    if answer==winner:
        print('answer is right')
        #clear
        os.system('cls' if os.name == 'nt' else 'clear')
        score=score+1
        if answer=='b':
            #winner gets reassigned
            celeb1=celeb2
            celeb1_country=celeb2_country
            celeb1_description=celeb2_description
            celeb1_follower=celeb2_follower
        #so the option a changes every certain amount
        if score%3==0:
            rand_celeb=random.randint(0,amount_names-1)
            celeb1=game.data[rand_celeb]['name']
            celeb1_follower=game.data[rand_celeb]['follower_count']
            celeb1_description=game.data[rand_celeb]['description']
            celeb1_country=game.data[rand_celeb]['country']
    #loser starts new game and shows score    
    else:
        new_game='n'
        #clear
        os.system('cls' if os.name == 'nt' else 'clear')
        new_game=input(f'answer is wrong final score is {score}. Input y to restart')
        score=0
        rand_celeb=random.randint(0,amount_names-1)
        celeb1=game.data[rand_celeb]['name']
        celeb1_follower=game.data[rand_celeb]['follower_count']
        celeb1_description=game.data[rand_celeb]['description']
        celeb1_country=game.data[rand_celeb]['country']
        
