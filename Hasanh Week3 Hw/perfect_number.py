""""
Date : 16.02.2022
Prepared by the Program : Hasan
Name Of The Program : Perfect Number

"""
###################################################

from functools import reduce


def my_perfect_number(n):               #In this section we define the function.
    my_list=[]
    for i in range (1,n):
        sum=0
        for j in range(1,i):            #determines the divisors of each number up to that number.
            if i%j==0:            
                sum+=j
        if sum==i:                    
            my_list.append(i)
            
    sum=reduce(lambda x,y : x+y ,my_list)
    return print("perfect numbers =  ",my_list,"\nSum of Perfect Numbers : ",sum)
    
###################################################
my_perfect_number(1000)
###################################################