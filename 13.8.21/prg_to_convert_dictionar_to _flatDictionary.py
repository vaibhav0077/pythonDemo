monthNames = []
monthNum = []
temp =  {}
noOfMonthNames = int(input("Enter number of months : "))

t = 0 
for x in range (0 ,noOfMonthNames ):
    t = monthNames.append(str(input("Enter Month Name : " )))

    print("Next Name :- ")

for xx in range (0 ,noOfMonthNames ):
    t  = monthNum.append(int(input("Enter Month number in sequence : " )))
    print(t)
    print("Next Number :- ")
temp = {"Months" : monthNames, "numbers" : monthNum}
print(temp)
fina = dict(zip(temp['Months'], temp['numbers']))
print(fina)
