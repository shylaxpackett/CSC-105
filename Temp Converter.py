# Name: Shyla Packett
# Assignment: Temp Converter

# Reflection:

# What I liked about this assignment: Learning how to convert tempertures. I thought it was very fun seeing the code in action.

# What I struggled with: Formating! I am really hopeful I did my formatting right this time.
#
# Explain how if/elif/else works and why you used it:

#An if statement checks a condition first. If it is false, an elif checks another condition. If none of the conditions are true, the else statement runs. I used this to check if the user entered F, C, or something else.

#3 things I learned on this assignment:

#   1. How if/elif/else works for writting code

#   2. The importance of making sure everthing writen in your code is just so. I forgot to indent something and my code wouldn't run. It took my awhile to figure out why.

#   3. Hopefully how to properly format my code.




print("Shyla's Temp Converter:")

fTempEnteredSAP = float(input("Enter a temperature: "))
sTempTypeSAP = input("Is the temp F for Fahrenheit or C for Celsius? ")

if sTempTypeSAP == "F" or sTempTypeSAP == "f":

    if fTempEnteredSAP > 212:
        print("Temp can not be > 212")
    else:
        fCelsiusSAP = (5.0 / 9) * (fTempEnteredSAP - 32)
        print("The Celsius equivalent is:", format(fCelsiusSAP, ".1f"))

elif sTempTypeSAP == "C" or sTempTypeSAP == "c":

    if fTempEnteredSAP > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheitSAP = (9.0 / 5.0) * fTempEnteredSAP + 32
        print("The Fahrenheit equivalent is:", format(fFahrenheitSAP, ".1f"))

else:
    print("Enter a F or C")
