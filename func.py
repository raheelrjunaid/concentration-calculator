def convertUp(value):
    value = value * 1000
    return value

def convertDown(value):
    value = value / 1000
    return value

def replaceLetter(str, letter):
    str = str.replace(letter, "")
    return str

def sciNotation(number):
    number = format(number, ".2e")
    return number