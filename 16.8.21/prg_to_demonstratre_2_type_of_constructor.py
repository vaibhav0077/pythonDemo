from typing import Callable


try:
    print("\n")
    class employee:

        def __init__(self, fname, lname, salary):
            self.fname = fname
            self.lname= lname
            self.salary = salary
            

        @classmethod
        def change_input_str(cls, emp_str):
            fname, lname, salary = emp_str.split("-")
            print("Values assigned succesfully")
            print("\n\n")

            return cls(fname, lname, salary)

    


    vaibhav = employee.change_input_str("vaibhav-patel-44000")


    print(vaibhav.fname)
    print(vaibhav.lname)
    print(vaibhav.salary)




except Exception as e:
    print("Errors Are : ", e)
    


else:
    print("\n\n")
    print("No errors")

finally:

    print("\n\n")
    print("Execution Completed")