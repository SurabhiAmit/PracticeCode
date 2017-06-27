def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    def age(year,month,day):
        
            
        n,y=0,0
        while(y<year):
        	if y%100!=0 and y%4==0:
        		n+=1
        		y+=1
        	elif y%400==0 :
        		n+=1
        		y+=1
        	else:
        		y+=1
        		   
        age_y =((year-1)*365)+n
        
        if year%100!=0 and year%4==0:
        	x=29
        elif year%400==0:
        	x=29
        else:
        	x=28	
        if month ==1:
            age_m=0
        if month ==2:
            age_m= 31
        if month ==3:
            age_m= 31+x
        if month ==4:
            age_m= 31+x+31
        if month ==5:
            age_m= 31+x+31+30
        if month ==6:
            age_m= 31+x+31+30+31
        if month ==7:
            age_m= 31+x+31+30+31+30  
        if month ==8:
            age_m= 31+x+31+30+31+30+31
        if month ==9:
            age_m= 31+x+31+30+31+30+31+31
        if month ==10:
            age_m= 31+x+31+30+31+30+31+31+30
        if month ==11:
            age_m= 31+x+31+30+31+30+31+31+30+31
        if month ==12:
            age_m= 31+x+31+30+31+30+31+31+30+31+30  
        age_d=day
        return age_y+age_m+age_d
    age2=age(year2,month2,day2)
    age1=age(year1,month1,day1)
    return age2-age1
    ##


# Test routine
print daysBetweenDates(2012,1,1,2012,2,28)
print daysBetweenDates(2012,1,1,2012,3,1)
print daysBetweenDates(2011,6,30,2012,6,31)
print daysBetweenDates(2000,1,1,2092,8,8)
print daysBetweenDates(1900,1,1,1999,12,31)
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,31), 367),
                  ((2000,1,1,2092,8,8), 33823 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()


OUTPUT:
========

58
60
367
33823
36523
Test case passed!
Test case passed!
Test case passed!
Test case passed!
Test case passed!