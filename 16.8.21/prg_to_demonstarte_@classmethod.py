
# haji thoduk doubtfull 6e ,not undersanfd 100%

class students:
    
    standard = 1

    def __init__(self, id, name, std):
        self.id = id
        self.name = name
        self.std = std

    def std_increase(self):
        self.std += self.standard

    @classmethod
    def change_std(cls, standard):
        cls.standard = standard







vaibhav = students(10, "vaibhav", 10)
akshat = students(11, "akshat", 7)


print("Vaibhav std : ",vaibhav.std)
print("Ak standard :", akshat.std)

akshat.std_increase()
print("Changed Std ak: ",akshat.std)

vaibhav.change_std(2)

vaibhav.std_increase()


print("Changed Std va: ",vaibhav.std)

akshat.std_increase()
print("Changed Std ak: ",akshat.std)







