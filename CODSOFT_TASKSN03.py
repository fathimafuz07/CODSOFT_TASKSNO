import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=""
    for i in range(length):
        password+=random.choice(characters)
    return password
while True:
     length=int(input("enter password length:"))
     password=generate_password(length)
     print("Generated password:",password)
     again=input("generate another?(y/n):")
     if again.lower()!="y":
      break
print("Goodbye!")
    
