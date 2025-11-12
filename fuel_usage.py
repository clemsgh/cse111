# The first function named main function.
def main():
    # Get three inputs from the user.
    odometer = float(input("Enter the first odometer reading (miles): "))
    odometer2 = float(input("Enter the second odometer reading (miles): "))
    gallons = float(input("Enter the gallons of gas used: "))

    # Calculate the fuel efficiency in both miles per gallon and liters per 100 kilometers.
    fuel_efficiency_mpg = miles_per_gallon(odometer, odometer2, gallons)
    fuel_efficiency_lp100km = lp100k_from_mpg(fuel_efficiency_mpg)

    # Display the results.
    print(f"Fuel efficiency in miles per gallon: {fuel_efficiency_mpg:.1f} mpg")
    print(f"Fuel efficiency in liters per 100 kilometers: {fuel_efficiency_lp100km:.2f} L/100km")

# The second function named miles_per_gallon.
def miles_per_gallon(odometer, odometer2, gallons):
    """
    Calculate the fuel efficiency in miles per gallon,and return the result.
    """
    miles_driven = odometer2 - odometer
    fuel_efficiency_mpg = miles_driven / gallons
    return fuel_efficiency_mpg

# The third function named lp100k_from_mpg.
def lp100k_from_mpg(fuel_efficiency_mpg):
    """
    Convert miles per gallon to liters per 100 kilometers, and return the result.
    """
    fuel_efficiency_lp100km = 235.215 / fuel_efficiency_mpg
    return fuel_efficiency_lp100km

# Call the main function to start the program.
main()