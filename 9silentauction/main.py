import os
import art
print(f"{art.logo}\n Welcome to our silent auction")
clear = lambda: os.system('cls')
bids={}

def start():
    Name=input("What's your name")
    price=input("How much are you willing to pay")
    
    x=0
    
    bids[Name]=price
    endgame=input("Do you wish to add more bidders? Press y for yes and n for no").lower()
    clear()
    if endgame=="y":
        start()
    else:
        y=0
        t=""
        for names in bids:
            x=bids[names]
            if int(x)>y:
                y=int(x)
        for names in bids:
            if str(y)==bids[names]:
                t=names
        print(f"{y} is the highest bid by {t}")
    
start()


