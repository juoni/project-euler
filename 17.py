#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


# anytime I have related data I should store them somewhere
# in particular if they are related by index (in sequence), put in list

# returns the English representation of number n

def english(n):
    if n == 0:
        return 'zero'
    s = tens(n % 100)
    n /= 100
    if n % 10 != 0:  # exists hundreth digit
        if s != '':
            s = 'and ' + s
        s = digit(n) + ' hundred ' + s
    n /= 10
    if n != 0:  # exists thousandth digit
        if s != '':
            s = 'and ' + s
        s = digit(n) + ' thousand ' + s
    return s


# string representation of 1/2 digit number

def tens(n):
    if n < 10:
        return digit(n)
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n >= 20 and n < 30:
        return 'twenty ' + digit(n % 10)
    elif n >= 30 and n < 40:
        return 'thirty ' + digit(n % 10)
    elif n >= 40 and n < 50:
        return 'forty ' + digit(n % 10)
    elif n >= 50 and n < 60:
        return 'fifty ' + digit(n % 10)
    elif n >= 60 and n < 70:
        return 'sixty ' + digit(n % 10)
    elif n >= 70 and n < 80:
        return 'seventy ' + digit(n % 10)
    elif n >= 80 and n < 90:
        return 'eighty ' + digit(n % 10)
    elif n >= 90 and n < 100:
        return 'ninety ' + digit(n % 10)
    else:
        sys.exit('tens: Should not reach this case')


# returns length of digit as a string

def digit(n):
    if n == 0:
        return ''  # this case is handled by caller
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    else:
        sys.exit('digit: number must be a digit. n:' + str(n))


s = 0
for i in xrange(1, 1001):
    print english(i)
    s += len(english(i).replace(' ', ''))
print 'Solution is:', s


