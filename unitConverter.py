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

match conversionNumber:
    case 1:
        toValue = fromValue / 1.609344
        print(f"{fromValue} {fromUnit} -> {toValue} {toUnit}")
    case 2:
        toValue = fromValue * 1.609344
        print(f"{fromValue} {fromUnit} -> {toValue} {toUnit}")
    case 3:
        toValue = fromValue * 2.20462262
        print(f"{fromValue} {fromUnit} -> {toValue} {toUnit}")
    case 4:
        toValue = fromValue / 2.20462262
        print(f"{fromValue} {fromUnit} -> {toValue} {toUnit}")
    case 5:
        toValue = (fromValue - 32.0) * (5.0 / 9.0)
        print(f"{fromValue} {fromUnit} -> {toValue} {toUnit}")
    case 6:
        toValue = (fromValue * (9.0 / 5.0)) + 32.0    
        print(f"{fromValue} {fromUnit} -> {toValue} {toUnit}")