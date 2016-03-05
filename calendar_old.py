#!/usr/bin/env python3

# -*- coding: iso-8859-1 -*-
def isLeapYear(year):
    if year %  4 ==  0 and year % 100 !=  0 or year % 400 ==  0:
        return True
    else:
        return False
 
def daysSince1900(year, month):
    days =  0
 
    for y in range(1900, year):
        days += 365
        if isLeapYear(y):
            days +=  1
    for m in range( 1, month):
        days += daysInMonth(year, m)
     
    #print 'daysSince1900', days
 
    return days
 
def daysInMonth(year, month):
    if month in ( 1,  3,  5,  7,  8, 10, 12):
        return 31
    elif month in ( 4,  6,  9, 11):
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28
 
 
def printCalendar(year, month):
    j = dayInWeek(year, month)
    for i in range( 1, j +  1):
        print('{:>5}'.format(''), end='')
    for day in range( 1,  1 + daysInMonth(year, month)):
        print('{:5d}'.format(day), end='')
        if (day + j) %  7 ==  0:
            print('\n')
    print('\n')
 
 
def dayInWeek(year, month):
    days = daysSince1900(year, month) +  1
    #print 'dayInWeek', days
    return days %  7
     
 
def printHeader():
    for i in ('Sun','Mon','Tues','Wed','Thur','Fri','Sat'):
        print('{:>5}'.format(i), end='')
    print('\n  ---------------------------------------')
#print '日  一  二  三  四  五  六'
 
year = int(input('year: '))
month = int(input('month: '))
print('\n')
 
printHeader()
printCalendar(year, month)
