
###########################################################
#
#  CSE 231 Project #3
#   Samuel Isken CSE 231 - 730 
#
#
#  Algorithm
#    prompt for file input
#    check to ensure file is in the same directory as our program
#    explores file line by line finding the minimum and maximum value of line 9 
#    then finds corresponding value in line 44 and year associated with the values 
#    prints all of this information with clean labels for data 
#    
############################################################




def open_file(): #This section is complete 
    '''Repeatedly prompt until a valid file name allows the file to be opened.'''
    
    #Checks for correct volume name using try and except
    prompt_checker = True 
    while prompt_checker == True:
        

        try:
            filename = input("Enter a file name: ")
            fp = open(filename, "r")
            prompt_checker = False
            return fp

        except FileNotFoundError:
            print("Error. Please try again")    
    


#Function to find the minumum percent change 
def find_min_percent(line):
    '''Find the min percent change in the line; return the value and the index.'''
    min_gdp_percent_checker = 10000000
    min_gdp_percent_index = 0
    x = 76 
    while x < 640:
        new_val = float(line[x:x+12])
        if min_gdp_percent_checker > new_val:
            min_gdp_percent_checker = new_val
            min_gdp_percent_index = x 
        x = x + 12    
    return min_gdp_percent_checker , min_gdp_percent_index


#Function to find the maximum percent change 
def find_max_percent(line):
    max_gdp_percent_checker = 0
    max_gdp_percent_index = 0
    x = 76 
    while x < 640:
        new_val = float(line[x:x+12])
        if max_gdp_percent_checker < new_val:
            max_gdp_percent_checker = new_val
            max_gdp_percent_index = x 
        x = x + 12    
    return max_gdp_percent_checker , max_gdp_percent_index


#Finds corresponding GDP values
def find_gdp(line, index):
    '''Use the index fo find the gdp value in the line; return the value'''
    gdp_value = float(line[index:index+12])
    return gdp_value


#Finds corresponding years 
def find_year(index):
    line_num = 0
    fp_GDP = open("GDP.txt", "r")
    for line in fp_GDP:
        line_num += 1
        if line_num == 8:
            year = (line[index:index+12])
    return year

#Function to display all the information
def display(min_val, min_year, min_val_gdp, max_val, max_year, max_val_gdp):
    '''Display values; convert billions to trillions first.'''    
    print("Gross Domestic Product")
    print("min/max     change  year   GDP (trillions)")
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("min" , min_val, int(min_year), min_val_gdp/1000))
    print("{:<10s}{:>8.1f}{:>6d}{:>18.2f}".format("max" , max_val, int(max_year), max_val_gdp/1000))
    
#Main body of our code where functions are executed after opening the data file 
def main(): 
    line_num = 0
    fp_GDP = open_file()
    for line in fp_GDP:
        line_num += 1
        if line_num == 9:
            min_value , min_value_index = find_min_percent(line)
            max_value , max_value_index = find_max_percent(line)
        if line_num == 44:
            min_gdp = find_gdp(line, min_value_index)
            max_gdp = find_gdp(line, max_value_index)
    min_year = find_year(min_value_index)
    max_year = find_year(max_value_index)
    #print((min_value, min_year, min_gdp, min_value, max_year, max_gdp))
    display(min_value, min_year, min_gdp, max_value, max_year, max_gdp)



# Calls the 'main' function only when you execute within Spyder (or console)
# Do not modify the next two lines.

if __name__ == "__main__":
    main()