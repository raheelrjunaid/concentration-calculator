def convertUp(value):
    return value * 1000


def convertDown(value):
    return value / 1000


def deleteLetter(string, letter):
    return string.replace(letter, "")


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


def promptUserUNIT(data_type, unit_base):
    while True:
        mila_unit = "m" + unit_base
        kilo_unit = "k" + unit_base
        options = f"{unit_base}, {mila_unit}, {kilo_unit}"
        data = input(f"Input total {data_type} of compound [{options}]: ")

        if data.lower().endswith(unit_base):
            if data.lower()[-2:] == mila_unit:
                return convertDown(float(deleteLetter(data, mila_unit)))
            elif data.lower()[-2:] == kilo_unit:
                return convertUp(float(deleteLetter(data, kilo_unit)))
            else:
                return float(deleteLetter(data, unit_base))

def promptNum(data_type, unit):
    while True:
        try:
            return float(input(f"Input compound {data_type} [{unit}]: "))
        except ValueError:
            print(f"{data_type} has to be a number.")
