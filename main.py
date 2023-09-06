print("CAESER CIPHER ")
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type encode or decode: \n ")
text = input("Enter a text: \n")
shift = int(input("Enter a shift number: \n "))

def e_display(e_text,e_shift):
    encode = " "
    for letters in e_text :
        position = alphabet.index(letters)
        new_position = position + e_shift
        new_letter = alphabet[new_position]
        encode+= new_letter
    print(f"The encoded text is: {encode}")

def d_display(d_text,d_shift):
    decode = " "
    for letters in d_text :
        position = alphabet.index(letters)
        new_position = position - d_shift
        new_letter = alphabet[new_position]
        decode+= new_letter
    print(f"The decoded text is: {decode}")


if direction == "encode":
    e_display(e_text=text, e_shift=shift)
elif direction == "decode":
    d_display(d_text=text, d_shift=shift)
