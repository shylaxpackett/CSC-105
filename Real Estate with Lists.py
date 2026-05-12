# Name: Shyla Packett

# Assignment: Real Estate with Lists

# Reflection:

# I really enjoyed this assignment. I thought it was fun seeing how my code could be used to calculate real estate sales which could be used for the future.

# I struggled with making sure my intails were in all the right spots. There was one place where I wasn't sure if it was a variable, to be safe I just put them there. 

# A list stores multiple values in one variable. It keeps the values in order and organized.

# A list could be used for our previous temperature project. The list could store all the temperatures to find what the average temperature was for a certain week or even longer.


# Function to get a valid number
def getFloatInputSAP(promptSAP):

    while True:

        try:
            numberSAP = float(input(promptSAP))

            # Check if number is greater than 0
            if numberSAP > 0:
                return numberSAP

            else:
                print("Number must be greater than 0.")

        except:
            print("Please enter a valid number.")


# Function to calculate median
def getMedianSAP(listSAP):

    # Sort the list
    listSAP.sort()

    countSAP = len(listSAP)

    # If list has odd amount of numbers
    if countSAP % 2 == 1:

        middleSAP = countSAP // 2
        return listSAP[middleSAP]

    # If list has even amount of numbers
    else:

        middleSAP = countSAP // 2

        medianSAP = (
            listSAP[middleSAP - 1] +
            listSAP[middleSAP]
        ) / 2

        return medianSAP


# Create empty list
salesListSAP = []

# Start loop
answerSAP = "Y"

while answerSAP == "Y" or answerSAP == "y":

    # Get sales value
    salesSAP = getFloatInputSAP(
        "Enter property sales value: ")

    # Add value to list
    salesListSAP.append(salesSAP)

    # Ask user if they want to continue
    answerSAP = input(
        "Enter another value Y or N: ")

    # Validate answer
    while (
        answerSAP != "Y" and
        answerSAP != "y" and
        answerSAP != "N" and
        answerSAP != "n" ):

        print("Please enter Y or N.")

        answerSAP = input(
            "Enter another value Y or N: ")


# Sort list
salesListSAP.sort()

# Display sorted list
print("\nSorted Sales Values")

for valueSAP in salesListSAP:

    print(f"${valueSAP:.2f}")


# Calculate values
minimumSAP = min(salesListSAP)

maximumSAP = max(salesListSAP)

totalSAP = sum(salesListSAP)

averageSAP = totalSAP / len(salesListSAP)

medianSAP = getMedianSAP(salesListSAP)

commissionSAP = totalSAP * 0.03


# Display results
print("\nResults")

print(f"Minimum: ${minimumSAP:.2f}")

print(f"Maximum: ${maximumSAP:.2f}")

print(f"Total: ${totalSAP:.2f}")

print(f"Average: ${averageSAP:.2f}")

print(f"Median: ${medianSAP:.2f}")

print(f"Commission: ${commissionSAP:.2f}")
