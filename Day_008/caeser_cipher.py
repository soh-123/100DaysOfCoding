from art import*
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(original_text, shift_amount):
    cipher_text = ""
    for element in original_text:
        if element in alphabet:
            position = alphabet.index(element)
            if direction == "encode":
                new_position = position + shift_amount
            elif direction == "decode":
                new_position = position - shift_amount
            else:
                print("Undefined number")
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += element
    print(f"Here's the {direction}d resault: {cipher_text}")

should_end = False
while should_end:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26

    caeser(original_text=text, shift_amount=shift)

    restart = input("Do you want to restart? Y or N\n")
    if restart == "n":
        should_end = True
    print("Good bye")



# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for element in original_text:
#         position = alphabet.index(element)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The new text is {cipher_text}")

# def decrypt (original_text, shift_amount):
#     decipher_text = ""
#     for element in original_text:
#         position = alphabet.index(element)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print(f"The new text is {decipher_text}")

# if direction == "encode":
#     encrypt(original_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(original_text=text, shift_amount=shift)
# else:
#     print("Undefined number")