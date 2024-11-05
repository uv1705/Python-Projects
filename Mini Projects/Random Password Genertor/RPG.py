#Random Password Genertor

import random
import string

pass_len=12
char_val = string.ascii_letters + string.digits + string.punctuation

password=""

for i in range(pass_len):
        password += random.choice(char_val)
        
print("your random password is: ",password)
        