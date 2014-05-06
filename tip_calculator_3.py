# Tip calculator code importing sys and using sys.argv

import sys

# create meal, tax and tip variables and assign them the relevant index of sys.argv
meal = float(sys.argv[1])
tax = float(sys.argv[2])
tip = float(sys.argv[3])

# create a variable tax_value and assign the value of the tax value
tax_value = meal * (tax / 100.0)

# create a variable meal_with_tax and assign it the value of meal + tax
meal_with_tax = meal + tax_value

# create a variable tip_value and assign it the value meal_with_tax * tip %
tip_value = meal_with_tax * (tip / 100.0)

# Create a variable total and assign it the value of the meal_with_tax + tip_value
total = meal_with_tax + tip_value

# print cost of the meal
print "The cost of your meal is ${0:.2f}".format(meal)

# print the $ value of tax the meal
print "You have to pay ${0:.2f} tax on your meal".format(tax_value)

# print the $ value of the tip and tip %
print "You have to pay ${0:.2f} in tips based {1} tip rate".format(tip_value, tip)

# print the grand total for the meal
print "The grand total for your meal is ${0:.2f}".format(total)



