""""
Date : 16.02.2022
Prepared by the Program : Hasan
Name Of The Program : Unique List

"""
###################################################
            
def uniq_list(my_list):                    #This function converts the values entered in the list to "set" and eliminates the same numbers.
    return (list(set(my_list)))            #It then returns these new numbers by converting them to "list" as well.
###################################################
print(uniq_list([1,2,3,3,3,3,4,5,5]))
###################################################   