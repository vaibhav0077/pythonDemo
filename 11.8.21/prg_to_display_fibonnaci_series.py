
f0 = 0
f1 = 1
f2 = f0 + f1


def fbDisplay(enterNum,f1, f2):

    print(str(f1), end=" ")
    
    if(f2 <= enterNum):
        fbDisplay(enterNum , f2, f1+f2)
    if f2 >= enterNum:
        print("\n\n\n")


enterNum = int(input("Enter Number Till fibonnaci Series displays : "))
print("\n\n\n")
print(str(f0), end=" ")
if enterNum >= f2 : 
    fbDisplay(enterNum,f1,f2 )