### Define a simple nextDay procedure, that assumes 
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if month==12 and day==30:                             #address change of year
        next_year,next_month,next_day=year+1,1,1
    elif month!=12 and day==30:                           #address change of month within a year
        next_year,next_month,next_day=year,month+1,1
    else:                                                 #address change of day within a month
        next_year,next_month,next_day=year,month,day+1
        
    return next_year,next_month,next_day
print nextDay(2013,12,30)
print nextDay(2087,1,30)
print nextDay(2076,2,4)

OUTPUT

(2014, 1, 1)
(2087, 2, 1)
(2076, 2, 5)