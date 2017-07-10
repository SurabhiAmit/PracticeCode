
# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(time):
    hou=time/(60*60)
    m=time % (60*60)
    minu=m/60
    s=m%60
    sec=s
    if int(hou)==1:
        hour='hour'
    else:
        hour='hours'
    if int(minu)==1:
        minute='minute'
    else:
        minute='minutes'
    if isinstance(sec,int) and sec==1:
        second='second'
    else:
        second='seconds'    
    ho=str(int(hou))
    mi=str(int(minu))
    se=str(int(sec))    
    if isinstance(sec,int):
        se=str(int(sec)) 
    else:
        se=str((sec))
    return ho+' '+ hour+","+' '+mi+ ' ' +minute+","+' '+se+' '+ second 
    
   
print convert_seconds(3600)

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
   
   
