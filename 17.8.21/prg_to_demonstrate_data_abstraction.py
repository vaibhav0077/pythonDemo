class employee:
    __count = 0

    def __init__(self) :
        employee.__count+=1

    def display(self):
        print(employee.__count)



emp = employee()

try:
    emp.display()

    # It will not run due to data abstraction
    print("Count is :",emp.__count)
    



except Exception:
    print("SOLVE THE ERRORS :")
    print(Exception)




