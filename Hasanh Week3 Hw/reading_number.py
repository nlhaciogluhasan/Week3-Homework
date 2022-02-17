""""
Date : 16.02.2022
Prepared by the Program : Hasan
Name Of The Program : Reading Number

"""
################################################################################################
def say_number(x):              #In this section we define the function.
    ones={1:"One", 2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    tens={1:"Ten",2:"Twenty",3:"Thirty",4:"Fourty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eigty",9:"Ninety"}
    tens1={11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}   
    
    one=x%10              # In this section, "one" and "ten" digits were determined.
    ten=x//10
        
    if x%10==0:       # If the entered number is a multiple of "10", it calls up the corresponding digit from the "ten" dictionary.
        print(x,"------------->",tens.get(ten))
    elif 10<x<20:
        print(x,"------------->",tens1.get(x))
    elif x<10:
        print(x,"------------->",ones.get(x))
    else:
        print(x,"------------->",tens.get(ten),ones.get(one))   
    
################################################################################################  
n=int(input("Enter a number : "))
say_number(n)
###################################################
    
    