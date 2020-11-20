def convertUp(value):
    value *= 1000
    return value

def convertDown(value):
    value /= 1000
    return value

def deleteLetter(str, letter):
    str = str.replace(letter, "")
    return str

def sciNotation(number):
    number = format(number, ".2e")
    return number

def molConvert(mass, volume, molar, mol1, mol2):
    return mass / molar, mass / molar / volume, mol1 * mass / molar / volume, mol2 * mass / molar / volume

def br(char):
    return "\n| " + char * 35 + "\n| "