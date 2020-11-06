def convertUp(value):
    value = value * 1000
    return value

def convertDown(value):
    value = value / 1000
    return value

def replaceLetter(str, letter):
    str = str.replace(letter, "")
    return str

# %w/v = g/ml
# ppm = mg/kg or mg/L
# M = mol/L

while True:
    mass = (input("Input total mass of compound: "))
    if mass.lower().endswith("g"):
        if mass.lower()[-2:] == "mg":
            mass = convertDown(float(replaceLetter(mass, "mg")))
            break
        elif mass.lower()[-2:] == "kg":
            mass = convertUp(float(replaceLetter(mass, "kg")))
            break
        else:
            mass = float(replaceLetter(mass, "g"))
            break
    else:
        print("Mass must be in g, mg or kg")

while True:
    volume = (input("Input total volume of compound: "))
    if volume.lower().endswith("l"):
        if volume.lower()[-2:] == "ml":
            volume = convertDown(float(replaceLetter(volume, "ml")))
            break
        elif volume.lower()[-2:] == "kl":
            volume = convertUp(float(replaceLetter(volume, "kl")))
            break
        else:
            volume = float(replaceLetter(volume, "l"))
            break
    else:
        print("Volume must be in l, ml or kl")

firstElement = input("Input first element in compound (no sub/superscript): ")
while True:
    try:
        firstMolAmount = int(input("Input first element molar quantity (2 for 2Pb):"))
        break
    except ValueError:
        print("Molar quantity has to be a number.")
secondElement = input("Input second element in compound (no sub/superscript): ")
while True:
    try:
        secondMolAmount = int(input("Input second element molar quantity (3 for 3Al):"))
        break
    except ValueError:
        print("Molar quantity has to be a number.")