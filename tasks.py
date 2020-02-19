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
