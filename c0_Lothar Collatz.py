c0= int(input("please enter a positive integer number (avoid negatives and zero)"))
counter = 0
while c0!= 1:
    if c0%2 ==0:
        c0 = c0/2
        print(int(c0))
        counter +=1
    else :
        c0 =3*c0+1
        print(int(c0))
        counter +=1
print("counter = ", counter)