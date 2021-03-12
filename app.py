from rich.console import Console
from rich.table import Table
from func import convertUp, molConvert
from func import sciNotation, promptUserUNIT, promptNum


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

# %w/v = g/ml
weight_volume_ratio = format(mass / convertUp(volume), ".2%")
# ppm = mg/kg or mg/L
ppm = convertUp(mass) / volume
data = molConvert(mass, volume, molarMass, firstMolAmount, secondMolAmount)

# Convert items to scientific notation for display purposes
for item in data:
    item = sciNotation(item)

mol = data[0]
mol_L = data[1]
firstElementConc = data[2]
secondElementConc = data[3]

# Generate columns
table = Table(title="Calculations", show_lines=True)
table.add_column("Title")
table.add_column("Result", style="green")
# Generate rows and fill with data + "units"
table.add_row("Percentage Concentration", weight_volume_ratio)
table.add_row("Parts Per Million", str(ppm) + " ppm")
table.add_row("Concentration", str(mol_L) + " mol/L")
table.add_row("Concentration of " + firstElement, str(firstElementConc) + " mol/L")
table.add_row("Concentration of " + secondElement, str(secondElementConc) + " mol/L")

# Print generated table
console = Console()
console.print(table)
