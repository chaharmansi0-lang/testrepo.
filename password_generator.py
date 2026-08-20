import random 
import string

letters=string.ascii_letters #a to z and A TO Z
digits=string.digits
symbols=string.punctuation

length=int(input("enter password length:"))

if length<4:
    print("password length should be at least 4")
else:
    password=[
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    all_characters = letters + digits + symbols

    for i in range(length-3): # we already have 3 characters for ex=8...then 8-3=5..then loop runs 5 times
        password.append(random.choice(all_characters))# each loop pick 1 random char. and add it to list

    random.shuffle(password)

    final_password="".join(password)#without it...password looks like this ['a','1','@','b','c','2]...
    print("\n generated password:",final_password)