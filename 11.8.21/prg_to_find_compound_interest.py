# A  = p / ( 1 + r/100 )^t
# Compound Interest A-p



principalAmount = int(input("Enter Principal Amount : "))
rate = int(input("Enter Rate (percentage) : "))
timeSpan = int(input("Enter Time Span (years) : "))


amount = principalAmount * pow( (1 + rate/100), timeSpan)

print("Total Amount Paid : ", amount)
print("Interest is : ", amount - principalAmount)