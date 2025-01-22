"""
    code for cypher text:
    Encryption

    logic:
        encrypt_txt = (input_txt + shift)
            if  if ('A'<=ch<='Z'):
                encrypt_txt = (ord(ch)-ord('A') + shift)%26 + ord('A')
"""


input_txt = input("Enter the Text for Encryption: ")
shift = int(input("Enter the value for Shift: "))

encrypt_txt = ""  # declaring an empty string
decrypted_txt = "" #decalring an empty string for decrypted_text

for ch in input_txt:
    if ('A'<=ch<='Z'):
        encrypted_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        decrypted_char = chr((ord(ch) - ord('A') - shift)%26 + ord('A'))
        encrypt_txt += encrypted_char #Appending 
        decrypted_txt += decrypted_char
print(encrypt_txt)
print(decrypted_txt)
   
