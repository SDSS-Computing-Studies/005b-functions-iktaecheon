#!python3

# def sum(a,b):
    #inputs
    # a : float 
    # b : float
    # return value: returns the sum of the 2 numbers



#this should return a value of 7
#x = sum(3,4)

#this should return a value of 12.5
#y = sum(11,1.5)


def sum(a,b): 
    answer = a + b
    if answer%1 == 0:
        answer = int(answer)
    return answer
