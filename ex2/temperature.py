
#################################################################
# FILE : temperature.py
# WRITER : Gaberiel Dubin  , dubingabie , 209386481
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: a simple program that checks if the temperature at vormir
#                is above a certain threshold on at least two out of three days
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################


def is_vormir_safe(threshold_temperature, day1_temp, day2_temp, day3_temp):
    """ a function that receives four parameters: a threshold temperature
        and the temperature of three adjacent days and checks  if the temperature
        of at least two out of the three days  is above the threshold temperature """
    temperature_list = [day1_temp, day2_temp, day3_temp]
    higher_temp_counter = 0
    for i in range(3):
        if temperature_list[i] > threshold_temperature:
            higher_temp_counter += 1
    return higher_temp_counter >= 2


