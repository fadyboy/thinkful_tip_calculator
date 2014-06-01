import sys
from tip_cal_functions import calculate_rate, calculate_meal_costs
import pdb

# display a friendly error message if a ValueError exception is raised

def main():
    while True:
        try:
            # assign user inputs for the cost of the meal, tax rate and tip rate
            #pdb.set_trace()
            meal = float(sys.argv[1])
            tax_rate = float(sys.argv[2])
            tip_rate = float(sys.argv[3])
            break


        except ValueError:

            print "Please enter a valid number for all your input parameters"
            meal = float(raw_input("Please enter a valid amount for the meal:"))
            tax_rate = float(raw_input("Please enter a valid amount for the tax rate:"))
            tip_rate = float(raw_input("Please enter a valid amount for the tip rate:"))
            break


    # Calculate the meal costs and print out using imported functions
    # pdb.set_trace()
    meal_info = calculate_meal_costs(meal, tax_rate, tip_rate)

    print "The base cost of your meal is ${:.2f}".format(meal_info['meal_base'])
    print "You need to pay ${:.2f} for tax".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should pay ${1:.2f} in tips".format(int(100 * meal_info['tip_rate']),
                                                                              meal_info['tip_value'])
    print "The grand total for you meal is ${:.2f}".format(meal_info['total'])


if __name__ == '__main__':

    main()