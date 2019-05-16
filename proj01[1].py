###########################################################
#
#  CSE 231 Project #1 
#   Samuel Isken CSE 231 - 730 
#
#
#  Algorithm
#    prompt for a real number of rods  
#    input a real number
#    converts to various units 
#    prints conversions and displays travel time 
#    ends computation      
#    
#
###########################################################


# User inputs number and it is converted to a real number 
str_rods = input("Input rods: ")
print("You input", float(str_rods) , "rods.")
float_rods = float(str_rods) 
print("")

#Titles section of computation 
print("Conversions")

# Variable Definitions / Conversions 
meters = float_rods * 5.0292   
feet = meters / 0.3048
miles = meters / 1609.34   
furlongs = float_rods / 40 
minutes = (miles / 3.1) * 60  

# Conversions printed with labels
print("Meters:", round(meters, 3)) 
print("Feet:", round(feet,3))
print("Miles:", round(miles,3)) 
print("Furlongs:", round(furlongs,3))
print("Minutes to walk", float_rods, "rods:", round(minutes,3)) 
