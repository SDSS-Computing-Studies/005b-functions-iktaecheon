#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
def hypotenuse(x,y,z):
    if z == True:
        ans = (x**2+y**2)**(1/2)
    elif z == False:
        if x > y:
            ans = (x**2-y**2)**(1/2)
        elif y > x:
            ans = (y**2-x**2)**(1/2)
    if ans %1 == 0:
        ans = int(ans)
    return ans
