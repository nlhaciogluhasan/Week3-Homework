""""
Date : 16.02.2022
Prepared by the Program : Hasan
Name Of The Program : Equal Reverse

"""
###################################################

def equal_reverse(myword):       #Returns TRUE if each word entered in this function is equal to its reverse writing.
    for i in myword:
        mylist=list(i)[:]
        mylist.reverse()
        print (mylist==list(i),end=",")

###################################################
n=list(input("Enter different words with ',' : ").split(","))
equal_reverse(n)
###################################################