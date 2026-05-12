# Name: Shyla Packett

# Assignment: Final Project

# Reflection:

# I liked learning how to make a banking system. It was interesting to see a possible way for abanking system to work. 

# It was interesting watching the code in action and seeing the change in the balances of the account after each tranaction.


# I struggled the most with loops and making sure the transaction history displayed correctly. 

#This semester, I learned how to use variables, arithmetic, if/elif/else statements, loops, functions, lists, string methods, and file processing in Python.
#Each assignment helped prepare me for this final project, because I practiced using different coding concepts step by step. #
#Earlier projects helped me understand user input, calculations, and formatting output.
#Learning loops helped me create menus that repeat until the user exits. Functions made the code easier to organize and read.
#This project helped me combine everything I have learned this semester into one simple code that is both efficient and functional

# Global Variables
fBalanceSP = 0.0
lstHistorySP = []


# Function to ask for valid input
def PromptForInputSP(sMessageSP):

    while True:

        try:
            fAmountSP = float(input(sMessageSP))

            if fAmountSP > 0:
                return fAmountSP

            else:
                print("Enter a number that is > 0")

        except:
            print("Invalid number entered")


# Deposit Function
def DepositSP():

    global fBalanceSP
    global lstHistorySP

    fDepositSP = PromptForInputSP("Enter deposit amount: ")

    fBalanceSP = fBalanceSP + fDepositSP

    sTransactionSP = "Deposit".ljust(20) + "$" + format(fDepositSP, ",.2f")
    lstHistorySP.append(sTransactionSP)

    print("Deposit successful! New balance: $" + format(fBalanceSP, ",.2f"))


# Withdraw Function
def WithdrawSP():

    global fBalanceSP
    global lstHistorySP

    fWithdrawSP = PromptForInputSP("Enter withdrawal amount: ")

    if fWithdrawSP > fBalanceSP:
        print("Withdrawal exceeds account balance")

    else:
        fBalanceSP = fBalanceSP - fWithdrawSP

        sTransactionSP = "Withdrawal".ljust(20) + "$" + format(fWithdrawSP, ",.2f")
        lstHistorySP.append(sTransactionSP)

        print("Withdrawal successful! New balance: $" + format(fBalanceSP, ",.2f"))


# Check Balance Function
def CheckBalanceSP():

    global fBalanceSP

    print("Current Balance: $" + format(fBalanceSP, ",.2f"))


# Transaction History Function
def TransactionHistorySP():

    global lstHistorySP

    print("----------------------------------------")
    print("Transaction History")
    print("----------------------------------------")

    if len(lstHistorySP) == 0:
        print("No transactions found")

    else:

        for sItemSP in lstHistorySP:
            print(sItemSP)

    print("----------------------------------------")


# Interest Application Function
def InterestApplicationSP():

    global fBalanceSP
    global lstHistorySP

    if fBalanceSP == 0:
        print("Balance is 0 and no interest will be calculated")

    else:

        fRateSP = PromptForInputSP("Enter interest rate: ")

        fInterestSP = fBalanceSP * (fRateSP / 100 / 12)

        fBalanceSP = fBalanceSP + fInterestSP

        sTransactionSP = "Interest".ljust(20) + "$" + format(fInterestSP, ",.2f")
        lstHistorySP.append(sTransactionSP)

        print("Interest applied: $" + format(fInterestSP, ",.2f"))
        print("New balance: $" + format(fBalanceSP, ",.2f"))


# Produce Statement Function
def ProduceStatementSP():

    global lstHistorySP

    objFileSP = open("spBankStatements.txt", "w")

    objFileSP.write("Transaction History\n")
    objFileSP.write("------------------------------\n")

    if len(lstHistorySP) == 0:
        objFileSP.write("No transactions found\n")

    else:

        for sItemSP in lstHistorySP:
            objFileSP.write(sItemSP + "\n")

    objFileSP.close()

    print("Statement file created")


# Main Function
def main():

    iOptionSP = 0

    print("Welcome to Shyla's Python Mini Banking System")

    while iOptionSP != 6:

        print()
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Calculate and Apply Interest")
        print("6. Exit")

        try:

            iOptionSP = int(input("Choose an option (1-6): "))

            if iOptionSP == 1:
                DepositSP()

            elif iOptionSP == 2:
                WithdrawSP()

            elif iOptionSP == 3:
                CheckBalanceSP()

            elif iOptionSP == 4:
                TransactionHistorySP()

            elif iOptionSP == 5:
                InterestApplicationSP()

            elif iOptionSP == 6:
                ProduceStatementSP()
                print("Thank you for using the banking system")

            else:
                print("Please choose a number between 1 and 6")

        except:
            print("Invalid menu option")


# Start Program
main()
