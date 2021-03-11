def convertUp(value):
    return value * 1000


def convertDown(value):
    return value / 1000


def deleteLetter(string, letter):
    modified_string = string.replace(letter, "")
    return modified_string


def sciNotation(number):
    return format(number, ".2e")


def molConvert(mass, volume, molar, firstMol, secondMol):
    mol = mass / molar
    mol_L = mol / volume
    firstConcentration = firstMol * mol_L
    secondConcentration = secondMol * mol_L
    return mol, mol_L, firstConcentration, secondConcentration


def br(char):
    return "\n| " + char * 35 + "\n| "
