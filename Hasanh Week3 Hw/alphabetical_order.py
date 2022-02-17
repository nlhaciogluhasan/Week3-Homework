""""
Date : 16.02.2022
Prepared by the Program : Hasan
Name Of The Program : Alphabetical Order

"""
###################################################

def alpha_order(words):               #In this section we define the function.
    words.sort()
    print("-".join(words))
###################################################

n=input("Please enter different words with'-' between them: ").split("-")
alpha_order(n)
###################################################