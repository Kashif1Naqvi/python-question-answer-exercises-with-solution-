"""
1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""

print("Twinkle,twinkle, little start,\n\t How I wonder what you are! \n \t\t Up above the world so high,\n \t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n \t How I wonder what you are!")


"""
2. Write a Python program to get the Python version you are using. Go to the editor

"""

import sys
print("python version",sys.version)
#python version 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)]
print("python version info",sys.version_info)
# python version info sys.version_info(major=3, minor=8, micro=1, releaselevel='final', serial=0)


"""
3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

now = datetime.datetime.now()
print(now.strftime("%y-%m-%d %H:%M:%S"))
# Output  =>  20-02-19 14:33:57

"""
4. Write a Python program which accepts the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math

r = float(input("Enter the radius of the cirle:"))
print(f"Radius of the circle str{r} is {math.pi*r**2} ")


"""
5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""
first_name = input("Enter the first name:")
last_name = input("enter the last name:")
print("Hello "+last_name + "  " + first_name )

"""Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
data = input("Sample data :")
list = data.split(',')
print(f"list is  {list} ")
print(f"tuple is {tuple(list)}")

"""
7. Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
"""
filename  = input("Sample filename :")
file_ext  = filename.split('.')
print("Output: ",file_ext[-1]) #file_ext[-1] I use because every time accept after dot end of the array index

"""
8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
"""
color_list = ["Red","Green","White" ,"Black"]
print("%s %s"%(color_list[0],color_list[-1]))
#OR
print(f"first color:> {color_list[0]} and last color is:=> {color_list[-1]} ")

"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (11, 12, 2014)

print("The examination will start from %i / %i / %i :"%(exam_st_date)) #%i or %s is format specifier that tell the type integer or string

"""
	10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
	Sample value of n is 5
	Expected Result : 615
"""
n = input("Sample value of n is ")
n1 = int("%s"% n)
n2 = int("%s%s"% (n,n))
n3 = int("%s%s%s"% (n,n,n))
print(n1+n2+n3)

"""
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""
print(abs.__doc__)

"""
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

import calendar
y = int(input("input the year:"))
m = int(input("input the month:"))

print(calendar.month(y,m))

# output:
#    February 2020
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29



""" other code:

    def pos_only_arg(*,arg):
        print(arg)
    pos_only_arg(arg=12)

    for i in range(19):
        print(i ,end='')

    def make_increment(n):
        return lambda x: x + n

    inc = make_increment(12)
    print(inc(2))
    print(inc(1))

    print(__doc__)


    matrix  = [
        [1,2,3,4],
        [3,4,5,6],
        [6,7,8,9]
    ]
    # show transpose of the matrix
    print( [[ row[i] for row in matrix ] for i in range(4) ])
    #output [(1, 3, 6), (2, 4, 7), (3, 5, 8), (4, 6, 9)]
     # same out put show by this function

    print(list(zip(*matrix)))
    #output [(1, 3, 6), (2, 4, 7), (3, 5, 8), (4, 6, 9)]


    question =['name','question','favorite color']
    answer=['kashif','What mean what?' ,'black']
    for q,a in zip(question,answer):
        print('What is your {0}? it is {1} '.format(q,a))
    output
        What is your name? it is kashif
        What is your question? it is What mean what?
        What is your favorite color? it is black


    # for reverse
    for i in reversed(range(1,10,2)):
        print(i)

    output:
        97531

    # for sorted
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(set(basket)):
        print(i)

    output:
            apple
            banana
            orange
            pear

    import math
    rawdata = [1,66,float('NaN'),2,3,4]
    filter_data = []
    for i in rawdata:
        if not math.isnan(i):
            filter_data.append(i)
    print(filter_data)
    # output:  [1, 66, 2, 3, 4]

"""
