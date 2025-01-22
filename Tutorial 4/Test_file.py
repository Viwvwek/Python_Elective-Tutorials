input_txt = input("Enter the Text for Encryption: ")
shift = int(input("Enter the value for Shift: "))

encrypt_txt = ""  # declaring an empty string
for ch in input_txt:
    if ('A'<=ch<='Z'):
        encrypted_char = chr((ord(ch) - ord('A') + shift)%26 + ord('A'))
        print(ord(ch))
        print(ord('A'))
        print(encrypted_char)
   
