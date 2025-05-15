






# CODER 

age = int(input("Quel est ton age "))
print(age)

while age < 0 : 
    print("erreur")
    age = int(input("Quel est ton age "))
print("ton age est", age)

if age >=  0 and age <=10:
    print("Tu es un enfant")
elif age >=11 and age < 18: 
    print("Tu es un adolescent ")
else:
    print("tu es un adulte")