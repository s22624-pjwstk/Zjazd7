import random
#zad1
names=("Łukasz","Zbyszek","Asia","Basia","Kasia")
print(names)
#zad2
surnames={"Kowalski","Wojewski","Karasiewicz","Currie"}
print(surnames)
#zad3
for x in names:
    if x[-1] == "a":
        print(x)
#zad4
print("----------------------")
def looks_like_polish_surname(s):
    polish_suffixes = ('ski', 'cki')
    for each in polish_suffixes:
        if s.endswith(each):
            return True
    return False
print(looks_like_polish_surname("Kowalski"))
print("----------------------")
#zad5
for x in surnames:
    if looks_like_polish_surname(x):
        print(x)
#zad6 i 7
people=[]
for x in names:
    for z in surnames:
        if x[-1]=="a" and z!="Karasiewicz":
            people.append(x+" "+z+"a")
        else:
            people.append(x+" "+z)
print("--------------------")
for x in people:
    print(x)

#zad8
#def create_person(name,surname):


#zad9
#random_nr=random.randint(0,100)
#zgadnij=int(input("podaj liczbe :"))
#while(zgadnij!=random_nr):
#    if zgadnij<random_nr :
#        print("Liczba za mała")
#        zgadnij = int(input("podaj liczbe :"))
#        zgadnij=random_nr
#    elif zgadnij>random_nr:
#        print("Liczba za duża ")
#        zgadnij = int(input("podaj liczbe :"))
#    else:
#        print(random_nr+"Zgadłeś")
#        zgadnij = int(input("podaj liczbe :"))

#zad10
i=1
while(i<=5):
    print("*"*i)
    i+=1
#zad11
print("--------")
i=5
while(i>=1):
    print("*"*i)
    i-=1
print("-----------")
#zad12
z=5
j=1
for x in range(5):
    x="*"
    print((z*" ")+(x*j)+(z*" "))
    z-=1
    j+=2
#zad13
print("-----------------")
i=0
while(i<5):
    print("*"*4)
    i+=1
#zad14