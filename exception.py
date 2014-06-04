import sys
# import functions from tip_cal_functions
from tip_cal_functions import calculate_meal_costs, calculate_rate


def main():
    # assign the value False to the variable done
    done = False
    try:
        # assign the user supplied inputs to the meal, tax_rate and tip_rate variables
        meal = float(sys.argv[1])
        tax_rate = float(sys.argv[2])
        tip_rate = float(sys.argv[3])

        # if valid input from sys.argv set done to True
        done = True

    except ValueError:
        # if a ValueError exception is thrown print friendly error message and prompt user for input
        print "Please enter valid numbers"

    while not done:
        try:
            meal = float(raw_input("Meal cost:"))
            tax_rate = float(raw_input("Tax rate:"))
            tip_rate = float(raw_input("Tip rate:"))

            # set done to True if valid input
            done = True

        except ValueError:
            print "You still need to enter a valid number!!"

    # assign the calculation of the meal costs to the variable meal_info
    meal_info = calculate_meal_costs(meal, tax_rate, tip_rate)

    # print details of meal
    print "The base cost of your meal is ${:.2f}".format(meal_info['meal_base'])
    print "You need to pay ${:.2f} for tax".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should pay ${1:.2f} in tips".format(int(100 * meal_info['tip_rate']),
                                                                              meal_info['tip_value'])
    print "The grand total for you meal is ${:.2f}".format(meal_info['total'])


if __name__ == "__main__":
    main()

