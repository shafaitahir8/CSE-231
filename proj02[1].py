
###########################################################
#
#  CSE 231 Project #2
#   Samuel Isken CSE 231 - 730 
#
#
#  Algorithm
#    prompt for inout price and dollars paid
#    check to ensure input is logical (follows standard rules of math and accounting)
#    checks for change starting with quarters and moving down to pennies 
#    prints change given and current stock 
#    prompts for next 
#    
############################################################
# purchase price and payment will be kept in cents
#Sets initial change amount available
quarters = 10
dimes = 10
nickels = 10
pennies = 10

#Finds dollar value of coins remaining
coin_sum = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01) 

#Initial introduction to the program 
print("\nWelcome to change-making program.")

print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))


#Prompts for price and then for dollars paid 
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
#Defines "change", denotes the money we will receive (difference between purchase price and dollars paid)
   



while in_str != 'q':
    in_flt = float(in_str)
    #Checks to ensure we have not inputted a negative number 
    if in_flt < 0:
        print("Error: purchase price must be non-negative.")
        print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
        in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        in_flt = float(in_str)
        
        
    #Keeps count of our money left    
    pay_int = int(input("Input dollars paid (int): "))
    change = pay_int - in_flt
    coin_sum = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01) 
    
    #checks to ensure that we have not inputted less $$$ than required
    if pay_int < in_flt:
        print("Error: insufficient payment.")
        pay_int = int(input("Input dollars paid (int): "))
        change = pay_int - in_flt
    #Checks to ensure we can pay
    if change > coin_sum:
        if  quarters != 10 or dimes != 10 or nickels != 10 or pennies != 10:
            print("Error: ran out of coins.")    
            break
        else:
            print("Error: insufficient payment.")
            break
    #Checks if money inputted is equivalent to cost 
    if in_flt == pay_int:
        print("No change.")
    
    #Finds number of quarters to give as change and keeps track of change given and change remaining
    number_of_quarters_used = int(change / .25)
    if number_of_quarters_used < quarters:
        quarters = quarters - number_of_quarters_used
    else:
        number_of_quarters_used = quarters
        quarters = quarters - number_of_quarters_used                  
    change = change - (number_of_quarters_used * .25)
    
    #Finds number of dimes to give as change and keeps track of change given and change remaining
    number_of_dimes_used = int(change / .10)
    if number_of_dimes_used < dimes:
        dimes = dimes - number_of_dimes_used
    else:
        number_of_dimes_used = dimes
        dimes = dimes - number_of_dimes_used         
    change = change - (number_of_dimes_used * .10) 
    
    #Finds number of nickels to give as change and keeps track of change given and change remaining
    number_of_nickels_used = int(change / .05)
    if number_of_nickels_used < nickels:
        nickels = nickels - number_of_nickels_used
    else:
        number_of_nickels_used = nickels
        nickels = nickels = number_of_nickels_used         
    change = change - (number_of_nickels_used * .05) 
    
    #Finds number of pennies to give as change and keeps track of change given and change remaining
    number_of_pennies_used = int(change / .01)
    if number_of_pennies_used < pennies:
        number_of_pennies_used = round(change / .01 , 2)
        pennies = pennies - number_of_pennies_used
    else:
        number_of_pennies_used = pennies
        pennies = pennies - number_of_pennies_used         
    change = change - (number_of_pennies_used * .01)    
    
    
    #Prints change collected 
    if in_flt != pay_int:
        print("Collect change below: ")    
        if number_of_quarters_used > 0:
            print("Quarters:" , number_of_quarters_used)
        if number_of_dimes_used > 0:
            print("Dimes:" , number_of_dimes_used)
        if number_of_nickels_used > 0:
            print("Nickels:" , number_of_nickels_used)
        if number_of_pennies_used > 0:  
            print("Pennies:" , int(number_of_pennies_used))
    
    #Prints remaining stock of change
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, int(pennies)))

    #Prompts within our while loop for the next input 
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    

