#Shyla Packett

#Assignment: Compound Innterest

#Reflection:

# I enjoyed creating my code step by step. I found it interesting to see the code play out at the end. 

# I struggled with making sure all of my initials were in the correct spots. Once I knew where I needed to put them it was a struggle to remember to keep adding them after each variable.

#The Princiapal Investment needed to be multiplied by the Compounding value, Interest Rate and Number of Periods in several diffent ways. Therefore, grouping the equaatioon with () makes the equation simplier to solve. 

#   1. I went over how to format for multiplication again as the calculations in this assignment are quite different than last weeks.

#   2. I believe the spacing is correct this time for the output. I went over that as well and am working on fixing my other assignment too.

#   3. I learned that it takes time to code. Before I started this assignment I sat for a bit and really thought how I wanted to code this and relooked over material tohelp me with it.



fPrincipalSAP = float(input("Enter the starting principal: "))
fRateSAP = float(input("Enter the annual interest rate (as percent): "))
iTimesSAP = int(input("How many times per year is the interest compounded? "))
iYearsSAP = int(input("For how many years will the account earn interest? "))

fRateSAP = fRateSAP / 100

fAmountSAP = fPrincipalSAP * (1 + fRateSAP / iTimesSAP) ** (iTimesSAP * iYearsSAP)

print("At the end of", iYearsSAP, "years you will have $", format(fAmountSAP, ".2f"))
