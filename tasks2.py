
"""
13. Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""

print("a string that you \"don't\" have to escape \
\nThis \
\nis a ....... multi-line \
\nheredoc string --------> example");
# or simple
print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")
"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
from datetime import date
d1 = date(2014,7,2)
d2 = date(2014,7,11)
diffrence = d2 - d1
print(diffrence.days,"Days")

"""15. Write a Python program to get the volume of a sphere with radius 6."""
import math
radius = float(input("Enter the radius of the sphere:"))
volume = (4/3*math.pi*radius**3)
print(f"the volumn of the sphere is:{volume}")


"""
16. Write a Python program to get the difference between a given number
    and 17, if the number is greater than 17 return double the absolute difference."""

number = int(input("enter the number:"))
if number > 17:
     print("double",(number - 17)  * 2)
else:
     print("diffrence",17-number)

"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

def thousand(n):
    return (abs(1000-n) <= 100 ) or (abs(2000 - n) <= 100 )
print(thousand(900)) # true
print(thousand(1800)) #false
print(thousand(1900)) #true

"""
18. Write a Python program to calculate the sum of three given numbers,
    if the values are equal then return three times of their sum.
"""

def sum(x,y,z):
    sum = x+y+z
    if x == y == z:
        return sum * 3
    else:
        return sum

print("sum of three given numbers :",sum(2,2,2))

"""
19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
    If the given string already begins with "Is" then return the string unchanged.
"""

def string(str):
    if len(str) > 2 and str[:2] == "Is":
        return str
    return "Is" + str

print(string("command"))

"""
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""

def copy(str,n):
    result = ""
    for i in range(n):
         result += str
    return result

print(copy("kashif",3))
print(copy(" ",3))
print(copy("shah",1))

"""
21. Write a Python program to find whether a given number (accept from the user) is even or odd,
    print out an appropriate message to the user.
"""
number = int(input("Enter a number:"))
if number % 2 == 0:
    print(f"number  {number} is even ")
else:
    print(f"number {number}  is odd ")

"""
22. Write a Python program to count the number 4 in a given list.
"""
def list(n):
    count = 0
    for num in n:
        if num == 4:
            count +=1
    return count
print(f"4 shows in {list([2,3,4,4,4,4,5,6])} times")
