# Name: Shyla Packett

# Assignment: Grade Analyzer

# Reflection:

# I enjoyed this assignment. I think this is a helpful code to have especially for students to check and see where they stand in classes. 

# For me the hardest part of this asssignment was making sure I labelled everything correctly

# if/else is used when there are only two possible choices I think of these as yes/no answers. if/elif/else is used when there are more than two choices. I think of this like you are trying to get a more thoughtout response. Both of these were used for the code  

# Share 3 things you learned on this assignment:

# 1. How my grades affect my overall test scores. Not entirely related to this course but something I learned.

# 2. The importance of making sure evry little detail is labeled.

# 3. Never forget to double or triple check your code. The smallest detail could be missed like a '/' and mess up the entire code. 

# Name input
strNameSAP = input("Enter name of person: ")

# Test scores input
fltTest1SAP = float(input("Enter Test 1 score: "))
fltTest2SAP = float(input("Enter Test 2 score: "))
fltTest3SAP = float(input("Enter Test 3 score: "))
fltTest4SAP = float(input("Enter Test 4 score: "))

# Check for negative scores
if (fltTest1SAP < 0 or fltTest2SAP < 0 or fltTest3SAP < 0 or fltTest4SAP < 0):
    print("Test scores must be greater than 0.")
    exit()

# Ask to drop lowest
strDropSAP = input("Do you wish to drop the lowest grade? Enter Y or N: ")

# Validate input
if strDropSAP != "Y" and strDropSAP != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# Calculate average
if strDropSAP == "Y":
    # Find lowest WITHOUT using min()
    if fltTest1SAP <= fltTest2SAP and fltTest1SAP <= fltTest3SAP and fltTest1SAP <= fltTest4SAP:
        fltAverageSAP = (fltTest2SAP + fltTest3SAP + fltTest4SAP) / 3
    elif fltTest2SAP <= fltTest1SAP and fltTest2SAP <= fltTest3SAP and fltTest2SAP <= fltTest4SAP:
        fltAverageSAP = (fltTest1SAP + fltTest3SAP + fltTest4SAP) / 3
    elif fltTest3SAP <= fltTest1SAP and fltTest3SAP <= fltTest2SAP and fltTest3SAP <= fltTest4SAP:
        fltAverageSAP = (fltTest1SAP + fltTest2SAP + fltTest4SAP) / 3
    else:
        fltAverageSAP = (fltTest1SAP + fltTest2SAP + fltTest3SAP) / 3
else:
    fltAverageSAP = (fltTest1SAP + fltTest2SAP + fltTest3SAP + fltTest4SAP) / 4

# Determine letter grade
if fltAverageSAP >= 97:
    strGradeSAP = "A+"
elif fltAverageSAP >= 94:
    strGradeSAP = "A"
elif fltAverageSAP >= 90:
    strGradeSAP = "A-"
elif fltAverageSAP >= 87:
    strGradeSAP = "B+"
elif fltAverageSAP >= 84:
    strGradeSAP = "B"
elif fltAverageSAP >= 80:
    strGradeSAP = "B-"
elif fltAverageSAP >= 77:
    strGradeSAP = "C+"
elif fltAverageSAP >= 74:
    strGradeSAP = "C"
elif fltAverageSAP >= 70:
    strGradeSAP = "C-"
elif fltAverageSAP >= 67:
    strGradeSAP = "D+"
elif fltAverageSAP >= 64:
    strGradeSAP = "D"
elif fltAverageSAP >= 60:
    strGradeSAP = "D-"
else:
    strGradeSAP = "F"

# Output (formatted to 1 decimal)
print(strNameSAP + "'s test average is: " + format(fltAverageSAP, ".1f"))
print("Letter Grade for the test is: " + strGradeSAP)
