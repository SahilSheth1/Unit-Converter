print("UNIT CONVERTER \n")

conversionsAvailable = [(1, "Kilometers (km)", "Miles (mi)"),
                        (2, "Miles (mi)", "Kilometers (km)"),
                        (3, "Kilograms (kg)", "Pounds (lbs)"),
                        (4, "Pounds (lbs)", "Kilograms (kg)"),
                        (5, "Fahrenheit (°F)", "Celsius (°C)"),
                        (6, "Celsius (°C)", "Fahrenheit (°F)")]

print("Conversions Available: \n")

for conversionNumber, fromUnit, toUnit in conversionsAvailable:
    print(f'{conversionNumber}). {fromUnit} -> {toUnit}')
    
print()
conversion = input("Enter the number of the conversion you wish to use: ")
conversionIndex = int(conversion) - 1

conversionNumber, fromUnit, toUnit = conversionsAvailable[conversionIndex]
print()

fromValue = float(input(f"Enter {fromUnit}: "))
print()

