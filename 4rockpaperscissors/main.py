import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



yo=input('What do you choose Type 1 for rock, type 2 for paper, type 3 for scissors\n')
you=int(yo)
comp=random.randint(1,3)
print(comp)
if comp == 3 and you == 3:
    print(f"it's a tie Your opponent picked\n{scissors}\n and you picked {scissors}")
elif comp == 2 and you == 3:
    print(f"You win Your opponent picked\n{paper}\n and you picked {scissors}")
elif comp == 1 and you == 3:
    print(f"You lose. Your opponent picked\n{rock}\n and you picked {scissors}")
elif comp == 3 and you == 2:
    print(f"You lost. Your opponent picked\n{scissors}\n and you picked {paper}")
elif comp == 3 and you == 1:
    print(f"You win Your opponent picked\n{scissors}\n and you picked {rock}")
elif comp == 2 and you == 2:
    print(f"it's a tie Your opponent picked\n{paper}\n and you picked {paper}")
elif comp == 1 and you == 1:
    print(f"it's a tie. Your opponent picked\n{rock}\n and you picked {rock}")
elif comp == 2 and you == 1:
    print(f"You lost. Your opponent picked\n{paper}\n and you picked {rock}")
elif comp == 1 and you == 2:
    print(f"You won. Your opponent picked\n{rock}\n and you picked {paper}")
else:
    print(f"write a number from 1-3")