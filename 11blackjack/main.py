import random
import art


def countcomp():
    totalcomp=0
    for comp in house:
        totalcomp+=comp
    return totalcomp

def countplayer():
    totalplayer=0
    for playr in player:
        totalplayer+=playr
    return totalplayer

def draw(user, amount):
    amount=int(amount)
    while amount != 0:
        amount=amount-1
        luck=random.randint(0, len(cards)-1)
        user.append(cards[luck])
        
    if user==house:
        print(f"cards drawn by computer are {house}")
    else:
        print(f"cards drawn by you are {player}")

new_game="y"

while new_game=="y":
    totalcomp=0
    totalplayer=0
    print(f"{art.logo}\n Welcome to Blackjack")    
    cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player=[]
    house=[]
    draw(house, 2)
    draw(player, 2)
    continue_game=input('Input "y" to get another hit, input any other key to stop').lower()
    if continue_game=="y":
        while continue_game=="y":
            draw(player, 1)
            continue_game=input('Input "y" to get another hit, input any other key to stop').lower()
        
   
    countcomp()
    
    countplayer()
    

    if countplayer()>21:
        print ('over 21 you lost')
    
    if countcomp()>21:
        print(f"computer overdrew to {countcomp()}. You win")
    
    if countcomp()<12:
        draw(house,1)
        
    
    if countcomp()>21:
        print(f"computer overdrew to {countcomp()}. You win")
    
    if countcomp()<countplayer() and totalplayer<21:
        draw(house, 1)
    if countcomp()>21:
        print(f"computer overdrew to {countcomp()}. You win")

    elif countplayer()>countcomp():
        print(f"player has {countplayer()}. Computer has {countcomp()}. You WIN")
        
    elif countcomp()>countplayer():
        print(f"player has {countplayer()}. Computer has {countcomp()}. You lost")
        

    new_game=input('play new game? input "y" for yes or anything else to end')
    if new_game=="y":
        print('new hand started')
    else:
        print('goodbye')
        

      
