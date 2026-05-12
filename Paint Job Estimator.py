
# Name: Shyla Packett

# Assignment: Paint Job Estimator

# Code Name: PaintEstimator

# Reflection Questions:

# I liked that this assignment helped me understand how to break a large problem into smaller parts using functions.

# I struggled the most with input validation as well as formatting.

# A function is a block of code that performs a specific task. To use it you call the function by its name and pass in the needed values and it can return a result.

# 1. One reason is that functions make code more organized and easier to understand.

# 2. Another reason is that they allow code to be reused, so you don’t have to rewrite the same logic multiple times.

import math

# Function to get validated float input
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: value must be greater than 0.")
            else:
                return value
        except:
            print("Error: please enter a valid number.")


def getGallonsOfPaint(fWallSpaceSAP, fFeetPerGallonSAP):
    return math.ceil(fWallSpaceSAP / fFeetPerGallonSAP)


def getLaborHours(fLaborHoursPerGallonSAP, iTotalGallonsSAP):
    return fLaborHoursPerGallonSAP * iTotalGallonsSAP


def getLaborCost(fLaborHoursSAP, fLaborChargePerHourSAP):
    return fLaborHoursSAP * fLaborChargePerHourSAP


def getPaintCost(iTotalGallonsSAP, fPaintPriceSAP):
    return iTotalGallonsSAP * fPaintPriceSAP


def getSalesTax(sStateSAP):
    sStateSAP = sStateSAP.upper()
    if sStateSAP == "CT":
        return 0.06
    elif sStateSAP == "MA":
        return 0.0625
    elif sStateSAP == "ME":
        return 0.085
    elif sStateSAP == "NH":
        return 0.0
    elif sStateSAP == "RI":
        return 0.07
    elif sStateSAP == "VT":
        return 0.06
    else:
        return 0.0


def showCostEstimate(sLastNameSAP, iGallonsSAP, fLaborHoursSAP, fPaintCostSAP, fLaborCostSAP, fTaxSAP, fTotalCostSAP):
    
    print(f"Gallons of paint: {iGallonsSAP}")
    print(f"Hours of labor: {fLaborHoursSAP}")
    print(f"Paint charges: ${fPaintCostSAP:.2f}")
    print(f"Labor charges: ${fLaborCostSAP:.2f}")
    print(f"Tax: ${fTaxSAP:.2f}")
    print(f"Total cost: ${fTotalCostSAP:.2f}")

    fileName = f"{sLastNameSAP}_PaintJobOutput.txt"
    
    with open(fileName, "w") as file:
        file.write(f"Gallons of paint: {iGallonsSAP}\n")
        file.write(f"Hours of labor: {fLaborHoursSAP}\n")
        file.write(f"Paint charges: ${fPaintCostSAP:.2f}\n")
        file.write(f"Labor charges: ${fLaborCostSAP:.2f}\n")
        file.write(f"Tax: ${fTaxSAP:.2f}\n")
        file.write(f"Total cost: ${fTotalCostSAP:.2f}\n")

    print(f"File: {fileName} was created.")


def main():
    fWallSpaceSAP = getFloatInput("Enter wall space in square feet: ")
    fPaintPriceSAP = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallonSAP = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallonSAP = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHourSAP = getFloatInput("Labor charge per hour: ")

    sStateSAP = input("State job is in: ")
    sLastNameSAP = input("Customer Last Name: ")

    iGallonsSAP = getGallonsOfPaint(fWallSpaceSAP, fFeetPerGallonSAP)
    fLaborHoursSAP = getLaborHours(fLaborHoursPerGallonSAP, iGallonsSAP)
    fPaintCostSAP = getPaintCost(iGallonsSAP, fPaintPriceSAP)
    fLaborCostSAP = getLaborCost(fLaborHoursSAP, fLaborChargePerHourSAP)

    fTaxRateSAP = getSalesTax(sStateSAP)
    fTaxSAP = (fPaintCostSAP + fLaborCostSAP) * fTaxRateSAP

    fTotalCostSAP = fPaintCostSAP + fLaborCostSAP + fTaxSAP

    showCostEstimate(sLastNameSAP, iGallonsSAP, fLaborHoursSAP, fPaintCostSAP, fLaborCostSAP, fTaxSAP, fTotalCostSAP)


# Run program
main()
