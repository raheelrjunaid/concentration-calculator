from func import *

# %w/v = g/ml
# ppm = mg/kg or mg/L
# M = mol/L

while True: # Validation
    mass = input("Input total mass of compound: ")
    if mass.lower().endswith("g"):
        if mass.lower()[-2:] == "mg":
            mass = convertDown(float(deleteLetter(mass, "mg")))
            break
        elif mass.lower()[-2:] == "kg":
            mass = convertUp(float(deleteLetter(mass, "kg")))
            break
        else:
            mass = float(deleteLetter(mass, "g"))
            break
    else:
        print("Mass must be in g, mg or kg")

while True: # Validation
    volume = input("Input total volume of compound: ")
    if volume.lower().endswith("l"):
        if volume.lower()[-2:] == "ml":
            volume = convertDown(float(deleteLetter(volume, "ml")))
            break
        elif volume.lower()[-2:] == "kl":
            volume = convertUp(float(deleteLetter(volume, "kl")))
            break
        else:
            volume = float(deleteLetter(volume, "l"))
            break
    else:
        print("Volume must be in l, ml or kl")

while True: # Validation
    try:
        molarMass = float(input("Input compound molar mass [g/mol]: "))
        break
    except ValueError:
        print("Molar Mass has to be only a number.")

firstElement = input("Input first element in compound (no sub/superscript): ")
while True: # Validation
    try:
        firstMolAmount = int(input("Input first element molar quantity (2 for 2Pb): "))
        break
    except ValueError:
        print("Molar quantity has to be a number.")
        
secondElement = input("Input second element in compound (no sub/superscript): ")
while True: # Validation
    try:
        secondMolAmount = int(input("Input second element molar quantity (3 for 3Al): "))
        break
    except ValueError:
        print("Molar quantity has to be a number.")

# Weight to Mass Conversions
w_v = format(mass / convertUp(volume), ".2%")
ppm = convertUp(mass) / volume

# Molar Conversions
# mol = mass / molarMass
# mol_L = mol / volume
# firstElementConc = firstMolAmount * mol_L
# secondElementConc = secondMolAmount * mol_L

mol, mol_L, firstElementConc, secondElementConc = molConvert(mass, volume, molarMass, firstMolAmount, secondMolAmount)

# Appearance
br = br("-")

# Return
print(f"\nResults:{br}Percentage Concentration: {w_v}{br}Parts Per Million: {sciNotation(ppm)} ppm {br}Molar Concentration: {sciNotation(mol_L)} mol/L {br}Molar Concentration of {firstElement} [{firstElement}] = {sciNotation(firstElementConc)} mol/L {br}Molar Concentration of {secondElement} [{secondElement}] = {sciNotation(secondElementConc)} mol/L\n")