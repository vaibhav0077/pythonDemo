# class is used for increase the code resuability
class employee:
    # Constructor
    increament = 1.5
    no_of_employeee = 0


    def __init__(self, fname, salary):
        self.fname = fname
        self.salary = salary
        employee.no_of_employeee+=1

    def increase_salary(self):
         self.salary = int(self.salary * employee.increament)

    # decorater
    @classmethod
    def change_in_increment(clls, amount):
        clls.increament = amount

# Objects of class employee

print("Total Employeee :" + str(employee.no_of_employeee))

vaibhav = employee("Patel", 20000)
print("King :  : " ,vaibhav.__dict__)
vaibhav.age = 20
print("King :  : " ,vaibhav.__dict__)

akshat = employee("Makwana" , 10000)
print("Ak : " , akshat.__dict__)


print("Total Employeee :" + str(employee.no_of_employeee))


# print("Employee Details : " , employee.__dict__)

# displaying values
# print(vaibhav.fname , vaibhav.salary)
# print(akshat.fname, akshat.salary)

# vaibhav.fname = "Patel"
# akshat.fname = "Makwana"

# vaibhav.salary = 1000
# akshat.salary = 2000






