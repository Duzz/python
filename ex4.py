print "Exercise 4: Variables and Names\n"

print "CODE\n"
# Set car variable to = 100 cars
cars = 100
# Set space in car to equal a floting point number of 4.0
space_in_a_car = 4.0
# Set total number of drivers to 30
drivers = 30
# Set total number of passengers to 90
passengers = 90
# Equation to find out number of cars not driven
cars_not_driven = cars - drivers
# Cars that are driven equal the number of drivers
cars_driven = drivers
# Equation to find carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Find average of passengers per car_driven
average_passengers_per_car = passengers / cars_driven

# Print out car variable
print "There are", cars, "cars available."
# Print drivers variable
print "There are only", drivers, "drivers available."
# Print cars not driven variable
print "There will be", cars_not_driven, "empty cars today."
# Print carpool variable
print "We can transport", carpool_capacity, "people today."
# Print passengers variable
print "We have", passengers, "to carpool today."
# Print average passengers per car
print "We need to put about", average_passengers_per_car, "in each car."

print "\nSTUDY DRILLS\n"

print "(1): I used 4.0 for 'space_in_a_car', but is that necessary? What happens if it's just 4?\n"
print "For this outcome having 'space_in_a_car' variable set to a floting point number is unnecessary. The outcome is just missing the following decimal points.\n"

print "(2): Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.\n"

print "(3): Write comments above each of the variable assignments.\n"

print "(4): Make sure you know what (=) is called (equals) and that it's making names for things.\n"

print "(5): Remember that (_) is and underscore character.\n"

print "(6): Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j."
