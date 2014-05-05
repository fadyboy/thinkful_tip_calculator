# Tip calculator exercise

# assign variable meal as base price of meal, tax(%) for tax on meal, and tip(%) for the tip on the meal
meal = 25.00
tax = 15.0
tip = 7.5

# create variable tax_value for the tax value on the meal
tax_value = meal * (tax / 100)

# create a variable meal_with_tax for the value of the meal + tax
meal_with_tax = meal + tax_value

# create a variable tip_value that taken from the meal_with_tax value
tip_value = meal_with_tax * (tip / 100)

# assign the variable total to be equal to meal_with_tax + tip_value
total = meal_with_tax + tip_value

# print the base cost of the meal
print "The base cost of your meal is ${:.2f}".format(meal)

# print the $ value of the tax on the meal
print "You have to pay ${:.2f} tax on your meal".format(tax_value)

# print the $ value of the tip based on the tip %
print "You have to pay ${:.2f} in tips based on {}% rate".format(tip_value, tip)

# print grand total for meal
print "The grand total for your meal is ${:.2f}".format(total)