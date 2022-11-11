alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
text=input("type your message: ").lower()
shift=int(input("type your shift number: "))
def encrypt(plain_text,shift_amt):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amt
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"the encoded text is {cipher_text}")

def decrypt(plain_text,shift_amt):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position-shift_amt
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"the encoded text is {cipher_text}")

if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)    
