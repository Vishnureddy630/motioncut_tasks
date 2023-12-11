#password generator for motion cut
import random
length=int(input("enter the length of the password :"))
n=int(input("enter the how many number of the password you want"))
nu= random.randint(1,10)
data=['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special_chars = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
al=random.choice(data)
AL = [letter.upper() for letter in data]
for j in range(n):
  for i in range(length):
    k=random.choice([data,AL,special_chars,[nu]])
    al+=str(random.choice(k))
  print(al)