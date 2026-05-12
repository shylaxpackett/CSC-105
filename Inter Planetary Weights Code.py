


#Name: Shyla Packett
#Assignment: Planetary Weights
#Reflection:
#I found it interesting finding out what my weight was on the different plantes in the solar system. I also simply enjoyed just practicing python code.

#For me the hardest part of this assignment was making sure everything lined up correctly with my formating.

#When making sure my output aligned I used print + format, one of the formatting optins we learned. As for the characters and decimal positions I found I needed to adjust those to make everything ling up right.

#Three things I learned:;
#   1. Which format option I find the easiest to code with.
#   2. How important it is to make sure everything is labeled in your code. If even the smallest thing is missing or not labeled correctly your code will not work.
#   3. Make sure to always double check your code for mistakes. While I was working on my code I missed a parenthesis and didn't notice it till I ran my code the first time. I will now be double checking every few lines after my mistake. 


#Weight factors of other planets

fMERCURY_FACTORSAP = 0.38

fVENUS_FACTORSAP = 0.91

fMOON_FACTORSAP = 0.165

fMARS_FACTORSAP = 0.38

fJUPITER_FACTORSAP = 2.34

fSATURN_FACTORSAP = 0.93

fURANUS_FACTORSAP = 0.92

fNEPTUNE_FACTORSAP = 1.12

fPLUTO_FACTORSAP = 0.066


sName= input("What is your name?")

sInput = input("What is your weight: ")

sEarthWeight = float(sInput)


print(sName + " here are your weights on our Solar System's planets: ")

# Planet Weight Calcuation

sPlanetWeight = fMERCURY_FACTORSAP* sEarthWeight
print(format("Weight on Mercury:","25s") , format(nMercury, '10.2f'))

sPlanetWeight = fVENUS_FACTORSAP* sEarthWeight
print(format("Weight on Venus:","25s") , format(nMercury, '10.2f'))

sPlanetWeight = fMOON_FACTORSAP* sEarthWeight
print(format("Weight on Moon:","25s") , format(nMercury, '10.2f'))


sPlanetWeight = fMARS_FACTORSAP* sEarthWeight
print(format("Weight on Mars:","25s") , format(nMercury, '10.2f'))

sPlanetWeight = fJUPITER_FACTORSAP* sEarthWeight
print(format("Weight on Jupiter:","25s") , format(nMercury, '10.2f'))

sPlanetWeight = fSATURN_FACTORSAP* sEarthWeight
print(format("Weight on Saturn:","25s") , format(nMercury, '10.2f'))

sPlanetWeight = fURANUS_FACTORSAP* sEarthWeight
print(format("Weight on Uranus:","25s") , format(nMercury, '10.2f'))

sPlanetWeight = fNEPTUNE_FACTOR* sEarthWeight
print(format("Weight on Neptune:","25s") , format(nMercury, '10.2f'))

fPlanetWeight = fPLUTO_FACTORSAP* sEarthWeight
print(format("Weight on Pluto:","25s") , format(nMercury, '10.2f'))





