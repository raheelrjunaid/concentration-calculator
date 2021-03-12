from func import convertUp, molConvert
from func import br, sciNotation, promptUserUNIT, promptNum

# %w/v = g/ml
# ppm = mg/kg or mg/L
# M = mol/L

try:
    mass = promptUserUNIT("mass", "g")
    volume = promptUserUNIT("volume", "l")
    molarMass = promptNum("molar mass", "g/mol")
    # First Compound Info
    firstElement = input("Input first element symbol in compound [Cl]: ")
    firstMolAmount = promptNum("molar quantity", "1")
    # Second Compound Info
    secondElement = input("Input second element symbol in compound [Cl]: ")
    secondMolAmount = promptNum("molar quantity", "1")
except KeyboardInterrupt:
    print('\nExited Program')
    quit()

# Weight to Mass Conversions
w_v = format(mass / convertUp(volume), ".2%")
ppm = convertUp(mass) / volume
data = molConvert(mass, volume, molarMass, firstMolAmount, secondMolAmount)
mol = data[0]
mol_L = data[1]
firstElementConc = data[2]
secondElementConc = data[3]

# Appearance
br = br("-")

# Return
print(f"\nResults:{br}Percentage Concentration: {w_v}{br}Parts Per Million: {sciNotation(ppm)} ppm {br}Molar Concentration: {sciNotation(mol_L)} mol/L {br}Molar Concentration of {firstElement} [{firstElement}] = {sciNotation(firstElementConc)} mol/L {br}Molar Concentration of {secondElement} [{secondElement}] = {sciNotation(secondElementConc)} mol/L\n")
