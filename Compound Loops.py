# Name: Shyla Packett

# Assignment: Compound Loops

# Reflection:

#   I enjoyed seeing how my code could be use to figure out compound interest.

#   I struggled with understanding when to use a while loop versus a for loop.

#   A for loop is used when you know how many times the loop will run. A while loop is used when the code needs to run for an unknow amount of time.

#   I used a for loop to calculate the balance over a fixed number of months because the number of months was given. I used a while loop to determine how many months it would take to reach the goal because that number was unknown.

#   I used a total of 6 loops in my code.


# 3 things I learned:

#   1. The importance of making sure everthing is labled and checked twice. I forgot the "P" in my intails in one line of code and messed up the code.

#   2. How compound interest works over time using loops.

#   3. The difference between for loops and while loops and when to use each.



# Deposit
while True:
    try:
        fDepositSAP = float(input("Enter deposit: "))
        if fDepositSAP > 0:
            break
        else:
            print("Deposit must be greater than 0.")
    except:
        print("Invalid input.")

# Interest Rate
while True:
    try:
        fRateSAP = float(input("Enter interest rate (%): "))
        if fRateSAP > 0:
            break
        else:
            print("Rate must be greater than 0.")
    except:
        print("Invalid input.")

# Months
while True:
    try:
        iMonthsSAP = int(input("Enter number of months: "))
        if iMonthsSAP > 0:
            break
        else:
            print("Months must be greater than 0.")
    except:
        print("Invalid input.")

# Goal
while True:
    try:
        fGoalSAP = float(input("Enter goal amount: "))
        if fGoalSAP >= 0:
            break
        else:
            print("Goal cannot be negative.")
    except:
        print("Invalid input.")

# Monthly rate
fMonthlyRateSAP = fRateSAP / 1200

# Loop for given months
fBalanceSAP = fDepositSAP

print("\n--- Monthly Growth ---")
for iMonthSAP in range(1, iMonthsSAP + 1):
    fBalanceSAP += fBalanceSAP * fMonthlyRateSAP
    print("Month", iMonthSAP, "- Balance: $", format(fBalanceSAP, ",.2f"))

# Loop to reach goal
fBalanceSAP = fDepositSAP
iCountSAP = 0

while fBalanceSAP < fGoalSAP:
    fBalanceSAP += fBalanceSAP * fMonthlyRateSAP
    iCountSAP += 1

print("\nMonths to reach goal:", format(iCountSAP, ","))

