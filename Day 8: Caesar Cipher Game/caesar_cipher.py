import string
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
char = string.ascii_lowercase
char = list(char)

def caesar(text, shift, direction):
    result = list(text)
    if direction == 'encode':
        for i in range(len(result)):
            # Wrap around to 'a' if exceeding 'z'.
            if result[i].isalpha():
                if ord(result[i]) + shift > ord('z'):
                    result[i] = chr(ord('a') + ((ord(result[i]) + shift) - ord('z')))
                else:
                    result[i] = chr(ord(result[i]) + shift)

    elif direction == 'decode':
        for i in range(len(result)):
            # Wrap around to 'z' if less than 'a'.
            if result[i].isalpha():
                if ord(result[i]) - shift < ord('a'):
                    result[i] = chr(ord('z') - ((ord('a') - (ord(result[i]) - shift))))
                else:
                    result[i] = chr(ord(result[i]) - shift)
    text = ''.join(result)
    print(f"Here's the {direction}d message: {text}")
    
while True:
    direction = input("Type 'encode' to encrypt, and 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26
    caesar(text, shift, direction)

    choice = input("\nType 'yes' if you want to go again, otherwise type 'no': ")
    if choice == 'no':
        print("\nThank you for using Caesar Cipher!")
        break
    elif choice != 'yes':
        print("\nInvalid Choice")
        break