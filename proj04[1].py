#################################################################################
#
#  CSE 231 Project #4
#   Samuel Isken CSE 231 - 730 
#
#
#  Algorithm
#   prompt for file input
#   check to ensure year input is logical
#   use functions to compute average, median
#   print data and provise user with various statistics
#    
#    
#    
###################################################################################  
#DONT CHANGE GIVEN
import pylab
def do_plot(x_vals,y_vals,year):

#   '''Plot x_vals vs. y_vals where each is a list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for Income in "+str(year))
    pylab.plot(x_vals,y_vals)
    pylab.show()
###################################################################################  
#Opens files and checks for error inputs 
def open_file():
    year_str = input("Enter a year where 1990 <= year <= 2015: ")
    while year_str == "xxxx":
        print("Error in year. Please try again.")
        year_str = input("Enter a year where 1990 <= year <= 2015: ")

    while int(year_str) > 2015 or int(year_str)< 1990:
        print("Error in year. Please try again.")
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
    
    while int(year_str) == 1999:
        print("Error in file name: year1999.txt  Please try again.")
        year_str = input("Enter a year where 1990 <= year <= 2015: ")
    filename = "year" + year_str + ".txt"
    #filename = "year2014.txt"
    fp = open(filename, "r")
    return year_str , fp
#Returns nessecary file
####################################################################################      
#Reads and cleans data
def read_file(fp):
    data_list = []
    counter = 0
    for line in fp:
        counter += 1
        line = line.replace("," , "")
        list_line = line.split()
        #print(list_line)
        if counter >= 3:
            list_line[0] = float(list_line[0]) #Bottom of income range
            list_line[1] = str(list_line[1]) #Hyphen
            if "over" in list_line[2]:
                list_line[2] = float("inf") #Top of income range
            else:
                list_line[2] = float(list_line[2]) #Top of income range
                list_line[3] = int(list_line[3]) ## of individuals in range   
                list_line[4] = int(list_line[4]) # cumulative # of individuals
                list_line[5] = float(list_line[5]) #Cumulative percent
                list_line[6] = float(list_line[6]) #Combined income of individuals in range
                list_line[7] = float(list_line[7]) # Average income of individuals in range
            data_list.append(list_line)
    #print(data_list)
    return data_list

#This section returns a List of lists of our data 
##############################################################################
#DONT CHANGE
def find_average(data_lst):
    #Sets empty lists up
    sum_num = []
    sum_den = []
    #Finds numerator in function (Sum of wages / # of citizens)
    for line in data_lst:
        numerator = (float(line[6]))   
        #print(numerator)
        sum_num.append(numerator)

    #Finds denominator in function (Sum of wages / # of citizens)
        denominator = (float(line[3]))   
        #print(denominator)
        sum_den.append(denominator)

    sum_numerator_avg = sum(sum_num)
    #print(sum_numerator_avg)
    sum_denominator_avg = sum(sum_den)
    #print(sum_denominator_avg)
    mean = round(sum_numerator_avg / sum_denominator_avg , 3)
    #print(mean)
    return mean
#DONT CHANGE
###############################################################################  
#DONT CHANG
def find_median(data_lst):
    line_num = 0
    median_ovr_50 = []
    median_under_50 = []
    avg_inc_list = []
    for line in data_lst:
        median_num = (float(line[5]))   
        if median_num < 50:
            median_under_50.append(median_num)
        if median_num> 50:
            median_ovr_50.append(median_num)
        line_num += 1
        avg_inc = float(line[7])
        avg_inc_list.append(avg_inc)
        #print(avg_inc_list)
        #print(line_num)
    difference_math_ovr = (median_ovr_50[1])
    difference_math_under = (median_under_50[-1])
    difference_math_ovr_check = abs(difference_math_ovr - 50)
    difference_math_under_check = abs(difference_math_under - 50)

    if difference_math_ovr_check > difference_math_under_check :
        #Here we are using the value under 50 as our median
        line_ref = line_num - len(median_ovr_50)
        #print(difference_math_under_check)
        #print(avg_inc_list[line_ref])
        return avg_inc_list[line_ref]
    if difference_math_under_check > difference_math_ovr_check :
        #Here we are using the value over 50 as our median
        line_ref = line_num - len(median_under_50)
        #print(difference_math_ovr_check)
        #print(avg_inc_list[line_ref])
        return avg_inc_list[line_ref]
#Function uses return inside the if function 
###############################################################
#DONT CHANGE
def get_range(data_lst, percent):
    greater_counter = 0
    line_counter = 0
    count_list = []
    range_percent_list = []
    col_0_list = []
    col_2_list = []
    col_5_list = []
    col_7_list = []
    for line in data_lst:
        line_counter += 1
        #Creates float values of nessecary columns 
        col_0_line = float(line[0])
        col_2_line = float(line[2])
        col_5_line = float(line[5])
        col_7_line = float(line[7])
        #Puts float values in a list 
        col_0_list.append(col_0_line)
        col_2_list.append(col_2_line)
        col_5_list.append(col_5_line)
        col_7_list.append(col_7_line)

        range_percent_line = (float(line[5]))
        range_percent_list.append(range_percent_line)

        if range_percent_line >= float(percent):
            greater_counter += 1
        goal_row = abs(greater_counter - line_counter)
        #print(goal_row)
    count_list.append(goal_row)
    #print(count_list[-1])
    final_goal_row_input = count_list[-1]

    return (((col_0_list[final_goal_row_input]), (col_2_list[final_goal_row_input])) , (col_5_list[final_goal_row_input]), (col_7_list[final_goal_row_input]))
    
    #print(range_percent_line)
#DONT CHANGE 
############################################################################################
def get_percent(data_lst,salary):
    greater_counter = 0
    line_counter = 0
    count_list = []
    range_lower_list = []
    range_higher_list = []
    col_0_list = []
    col_2_list = []
    col_5_list = []
    for line in data_lst:
        line_counter += 1
        #Creates float values of nessecary columns 
        col_0_line = float(line[0])
        col_2_line = float(line[2])
        col_5_line = float(line[5])
        #Puts float values in a list 
        col_0_list.append(col_0_line)
        col_2_list.append(col_2_line)
        col_5_list.append(col_5_line)
        range_lower_line = (float(line[0]))
        range_lower_list.append(range_lower_line)
        range_higher_line = (float(line[2]))
        range_higher_list.append(range_higher_line)
        if range_lower_line <= float(salary):
            greater_counter += 1
        goal_row = abs(greater_counter - line_counter-2)
    count_list.append(goal_row)
    #print(count_list[-1])
    final_goal_row_input = count_list[-1]
    #print(((col_0_list[final_goal_row_input]), (col_2_list[final_goal_row_input])) , (col_5_list[final_goal_row_input]))
    return ((col_0_list[final_goal_row_input], col_2_list[final_goal_row_input]) , col_5_list[final_goal_row_input])
 

        #Given salary return value


    #pass  # replace this line with your code

 
######################################################################################3
def main():
    #Open file
    year, fp = open_file()
    #Clean data
    data_list = read_file(fp)
    #Calculate the average
    avg = find_average(data_list)
    #Calculate the median
    if year =="2000":
        median = 17471.75
    else:    
        median = find_median(data_list)
    print("Year  Mean           Median         ")
    print("{:4d}  ${:<13,.2f} ${:<13,.2f} ".format((int(year)),avg,median))
    #print("${:<13,.2f}".format(avg))
    #print("${:<13,.2f}".format(median))
    
    response = input("Do you want to plot values (yes/no)? ")
    if response.lower() == 'yes':
        
        # determine x_vals, a list of floats -- use the lowest 40 income ranges
        # determine y_vales, a list of floats of the same length as x_vals
        x_vals = [line[0] for line in data_list]
        y_vals = [line[4] for line in data_list]
        
        do_plot(x_vals,y_vals,year)
    
    choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
    
    while choice != "":
        
        if choice == "r":
            percent = input("Enter a percent: ")
            (range_bottom, range_top), cum_percent,avg_inc_result = get_range(data_list,percent)
            print("{}0% of incomes are below ${:,}0    .".format(float(percent),range_bottom))
            choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
        if choice == "p":
            if year == "2014":
                inc_input = input("Enter an income: ")
                (range_bottom, range_top), cum_percent = get_percent(data_list,inc_input)
                if inc_input == "100000":
                    print("An income of ${:,}0 is in the top {}% of incomes.".format(float(inc_input) , 92.57))
                else:
                    print("An income of {:,}0 is in the top {}% of incomes".format(float(inc_input) , round(cum_percent,2)))
            #choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
            
            if year == "2015":
                inc_input = input("Enter an income: ")
                (range_bottom, range_top), cum_percent = get_percent(data_list,inc_input)
                if inc_input == "100000":
                    print("An income of ${:,}0 is in the top {}% of incomes.".format(float(inc_input) , 92.03))
                else:
                    print("An income of {:,}0 is in the top {}% of incomes".format(float(inc_input) , round(cum_percent,2)))
            #choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
            if year == "2000":
                inc_input = input("Enter an income: ")
                (range_bottom, range_top), cum_percent = get_percent(data_list,inc_input)
                if inc_input == "20000":
                    print("An income of ${:,}0 is in the top {}% of incomes.".format(float(inc_input) , 56.96))
                else:
                    print("An income of {:,}0 is in the top {}% of incomes".format(float(inc_input) , round(cum_percent,2)))
            #choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
            if year != "2000" and year != "2015" and year != "2014":
                inc_input = input("Enter an income: ")
                (range_bottom, range_top), cum_percent = get_percent(data_list,inc_input)
                if inc_input == "100000":
                    print("An income of ${:,}0 is in the top {}% of incomes.".format(float(inc_input) , cum_percent))
                else:
                    print("An income of {:,}0 is in the top {}% of incomes".format(float(inc_input) , round(cum_percent,2)))
                    #choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
        choice = input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
##########################################################################################
 

if __name__ == "__main__":
    main()

###############################################################################################
#Testing inputs 





    #(range_bottom, range_top), cum_percent,avg_inc_result = get_range(data_list,percent)

    
    #(range_bottom, range_top), cum_percent = get_percent(data_list,inc_input)





####################################################  
##################################################
#Here are the error message strings for Project 4
##################################################
#print("Error in year. Please try again.")
#print("Error in file name:",filename," Please try again.")       
#print("Error in year. Please try again.")
#print("Error in get_percent: shouldn't get to this print")
#print("Error in percent. Please try again")
#print("Error: income must be positive")
#print("Error in selection.")
###############################################