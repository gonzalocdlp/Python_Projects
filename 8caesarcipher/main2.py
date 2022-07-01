import art

def start():    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #Don't change the code above 👆

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(plain_text, shift_amount, encoder):
        if shift_amount>26:
            shift_amount=shift_amount%26
        cipher_text = ""
        for letter in plain_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                position = alphabet.index(letter)
                if direction=="encode":
                    new_position = position + shift_amount
                    d="encoded"
                else:
                    new_position = position - shift_amount
                    d="decoded"
                new_letter = alphabet[new_position]
                cipher_text += new_letter
        print(f"The {d} text is {cipher_text}")
        endgame=input  ("start again? press y. Input any other key to end")
        if endgame=="y":
            start()
        else:
            print("goodbye :]")

    encrypt(plain_text=text, shift_amount=shift, encoder=direction)    
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
print(art.logo)
start()


