#Podatek

n=int(input("Input amount: "))
if n <= 5000:
    n = (n)*0.17
    print(n)
else:
    if n > 5000:
        r=((n)-5000)*0.32
        n = 5000*0.17
        print(int(r)+int(n))

    
        