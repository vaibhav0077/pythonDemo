import csv

with open("python.csv", 'w') as csvfile:
    fieldname = ['fname', 'lname', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldname)
    # Just Writing the Column Names Above the file
    # writer.writeheader()

    writer.writerow({'fname':"vaibhav", "lname":"Patel", 'age':20})