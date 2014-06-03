import sys
from tip_cal_functions import calculate_rate, calculate_meal_costs

# display a friendly error message if a ValueError exception is raised

def main():
    # assign user supplied inputs for the cost of the meal, tax rate and tip rate
    try:
        meal = float(sys.argv[1])
        tax_rate = float(sys.argv[2])
        tip_rate = float(sys.argv[3])

    except ValueError:
        print "Please enter valid numbers"

        # assign the value False to a variable done which forms the break for a while loop if valid input entered
        done = False
        # prompt the user to enter valid input until valid input is supplied
        while not done:
            try:
                meal = float(raw_input("Please enter a valid number for the meal:"))
                tax_rate = float(raw_input("Please enter a valid number for the tax rate:"))
                tip_rate = float(raw_input("Please enter a valid number for the tip rate: "))

                # set the done variable to True if no exception is thrown
                done = True

            except ValueError:
                print "You still need to enter a valid numbers! "

    # Calculate the meal costs and print out using imported functions
    meal_info = calculate_meal_costs(meal, tax_rate, tip_rate)

    print "The base cost of your meal is ${:.2f}".format(meal_info['meal_base'])
    print "You need to pay ${:.2f} for tax".format(meal_info['tax_value'])
    print "Tipping at a rate of {0}%, you should pay ${1:.2f} in tips".format(int(100 * meal_info['tip_rate']),
                                                                              meal_info['tip_value'])
    print "The grand total for your meal is ${:.2f}".format(meal_info['total'])


if __name__ == '__main__':

    main()