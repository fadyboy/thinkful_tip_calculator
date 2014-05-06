# Tip calculator exercise
# import sys to use sys.argv to implement tip calculator using arguments

import sys

# create variable tax_value for the tax value on the meal
tax_value = float(sys.argv[1]) * (float(sys.argv[2]) / 100.0)


# create a variable meal_with_tax for the value of the meal + tax
meal_with_tax = float(sys.argv[1]) + tax_value

# create a variable tip_value that taken from the meal_with_tax value
tip_value = meal_with_tax * (float(sys.argv[3]) / 100.0)

# assign the variable total to be equal to meal_with_tax + tip_value
total = meal_with_tax + tip_value

# print the base cost of the meal
print "The base cost of your meal is ${0:.2f}".format(float(sys.argv[1]))

# print the $ value of the tax on the meal
print "You have to pay ${0:.2f} tax on your meal".format(tax_value)

# print the $ value of the tip based on the tip %
print "You have to pay ${0:.2f} in tips based on {1}% rate".format(tip_value, float(sys.argv[3]))

# print grand total for meal
print "The grand total for your meal is ${0:.2f}".format(total)