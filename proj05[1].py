##################################################################################
#
#  CSE 231 Project #5
#   Samuel Isken CSE 231 - 730 
#
#
#  Algorithm
#   prompt for file input
#   use functions to compute average, median of each crop and each state 
#   print data and provide user with various statistics
#    
#    
#    
###################################################################################  

#import csv

#proj05
#State Crop "All GE Varieties" Year Value(in percent)
STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
#Sets up STATES variable and initial dictionary 
state_dict = {}
def open_file():
    '''Inputs file'''
    filename = input("Enter a file: ")
    #filename_two = input("")
    #filename = "alltablesGEcrops.csv"
    fp = open(filename, "r")
    #print(fp)
    return fp
#############################################################################################
def read_file(file):
    '''Goes through file and ensure data is clean and ready for analysis'''    
 
    state_dict = {} #Keyed by state returns crop 
    for state in STATES:
        state_dict[state] = {}
    file.readline() #Skips header 
    for line in file:
        list_data = line.strip().split(",")
        state = list_data[0].strip()
        crop = list_data[1]
        variety  = list_data[3]
        year = int(list_data[4])
        value = list_data[6] #May not be an int
        #Let's clean the data here 
    
       # if state in STATES:    
        if variety == "All GE varieties":
            if state != "U.S.":
                if state != "Other States":
                    
                    state = list_data[0].strip()
                    if state == "Missouri 2/":
                        state = "Missouri"
                    crop = list_data[1]
                    variety  = list_data[3]
                    year = (list_data[4])
                    value = list_data[6] #May not be an int
                    try:
                        value = int(value)
                        pass
                    except:
                        value = 0
                    
                    #print(state,crop,variety,year,value)
                    #Now that we pulled the data we want to examine lets put it in a dictionary 
                    
                    if value > 0:
                        
                        if crop in state_dict[state]:
                            state_dict[state][crop][year] = value
                        else:
                            state_dict[state][crop] = {}
                            state_dict[state][crop][year] = value
                        
    
     
    return state_dict
#############################################################################
def get_crops(state_data):
    '''Pulls crops and sorts'''
    CROPS = [] #tuple of crops 
    for state in state_data:
        for crop in state_data[state]:
            CROPS.append(crop)
    crop_set = set(CROPS)
    crop_set = list(crop_set)
    crop_set.sort()
    #print(crop_set)
    
   
    
    return crop_set
############################################################################
def get_crop_stats(CROPS , state_data): 
    '''Data analysis function.  Calculates various statistics from data file'''
    #calc min max values
    #cal min max years 
    
    #Finds unique set of states 
    STATES_LIST = []
    for state in state_data:
        STATES_LIST.append(state)
    STATES_SET = set(STATES_LIST)
    #print(STATES_SET)
    crop_stats = {}
    for crop in CROPS:
        crop_stats[crop] = {}
        for state in STATES_SET:
            if crop in state_data[state]:
                min_val = 100
                max_val = 0
                #min_year = 100000
                #max_year = 1
                #print(state_data[state][crop])
                for (year , percent) in state_data[state][crop].items(): 
                    #print(year, percent)
                    if int(percent) > max_val:
                        max_val = int(percent)
                        max_year = year
                        if int(percent)  == max_val:
                            if int(year) < int(max_year):
                                max_year = year

                        
                    if int(percent) < min_val:
                        min_year = year
                        min_val = int(percent)
                        if int(percent)  == min_val:
                            if int(year) < int(min_year):
                                min_year = year
                        
                        
    
                #results = [state , crop, max_year, max_val, min_year, min_val]
                #print(results)
                crop_stats[crop][state] = [max_year,max_val,min_year,min_val]
                
    return crop_stats


##################################################################################
def main():
    fp = open_file()
    state_data = read_file(fp)
    CROPS = get_crops(state_data)
    crop_stats = get_crop_stats(CROPS , state_data)     
    for crop in CROPS:
        print("Crop:", crop)
        print("{:<20}{:<8}{:<6}{:<8}{:<6}".format("State","Max Yr","Max","Min Yr","Min"))
        for state in STATES:
            if crop in state_data[state]:
                max_year = crop_stats[crop][state][0]
                max_val = crop_stats[crop][state][1]
                min_year = crop_stats[crop][state][2]
                min_val = crop_stats[crop][state][3]
                
                print("{:<20}{:<8}{:<6}{:<8}{:<6}".format(state,max_year,max_val,min_year,min_val))    
########################################################################################

main()

#if __name__ == "__main__":
    #main()

##################################################################################