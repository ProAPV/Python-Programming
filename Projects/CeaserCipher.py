#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))\

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"


# def CeaserCipher(direction, text, shift):
#     EncodedText = ""
#     for x in range(len(text)):
#         if (alphabet.index(text[x]))+shift <= (len(alphabet))-1 | (alphabet.index(text[x]))-shift >= 0:
#             if direction == "encode":
#                 EncodedText+=alphabet[(alphabet.index(text[x]))+shift]
#             elif direction == "decode":
#                 EncodedText+=alphabet[(alphabet.index(text[x]))-shift]
#         elif (alphabet.index(text[x]))+shift > (len(alphabet))-1 | (alphabet.index(text[x]))-shift < 0:
#             if direction == "encode":
#                 number = ((alphabet.index(text[x]))+shift)%(len(alphabet))
#                 EncodedText+=alphabet[number]
#             elif direction == "decode":
#                 number = len(alphabet) + (alphabet.index(text[x])-shift)
#                 EncodedText+=alphabet[number]
#     print(EncodedText)

def ceaserCipher(direction, text, shift):
    EncodedText = ""
    if direction == "encode":
        for x in range(len(text)):
            if (alphabet.index(text[x]))+shift <= (len(alphabet))-1:
                EncodedText+=alphabet[(alphabet.index(text[x]))+shift]
            elif (alphabet.index(text[x]))+shift > (len(alphabet))-1:
                number = ((alphabet.index(text[x]))+shift)%(len(alphabet))
                EncodedText+=alphabet[number]
    elif direction == "decode":
        for y in range(len(text)):
            if (alphabet.index(text[y]))-shift >= 0:
                EncodedText+=alphabet[(alphabet.index(text[y]))-shift]
            elif (alphabet.index(text[y]))-shift < 0:
                number = len(alphabet) + (alphabet.index(text[y])-shift)
                EncodedText+=alphabet[number]
    print(EncodedText)
            
ceaserCipher(direction, text, shift)