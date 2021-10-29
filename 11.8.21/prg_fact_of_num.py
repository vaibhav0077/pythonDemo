def fact(x):
    if x < 0 :
        print("Negative Number have No Factorial")
        return None
    
    if x == 0 :
        return 1

    else:
        if x==1:
            return x

        else : 
            return x*fact(x-1)


a = fact(int(input("Enter a Number : ")))

print("Factorial Of entered number is : ", a)


