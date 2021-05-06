n=int(input("Wprowadz liczbę:"))

for x in range(n):
    if x==0 or x==n-1:
        x="*"
        print(x*3)
    elif x<n:
        x = "*"
        print(x+" "+x)
