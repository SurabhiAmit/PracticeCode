# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
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
    second='seconds'    
    ho=str(int(hou))
    mi=str(int(minu))
    se=str(sec)
    p=se.find(".")
    if int(se[p+1:])==0:
        se=str(int(sec))
        if int(sec)==1:
            second='second'
    return ho+' '+ hour+","+' '+mi+ ' ' +minute+","+' '+se+' '+ second
    
def download_time(file,file_unit,bw,bw_unit):
    if file_unit=='GB':
        file_size = 2 ** 30 * 8
    if file_unit=='MB':
        file_size=2 ** 20 * 8
    if file_unit=='TB':
        file_size=2 ** 40 * 8
    if file_unit=='kB':
        file_size=2 ** 10 * 8
    if file_unit=='kb':
        file_size=2 ** 10
    if file_unit=='Gb':
        file_size=2 ** 30
    if file_unit=='Tb':
        file_size=2 ** 40
    if file_unit=='Mb':
        file_size=2 ** 20
        
    if bw_unit== 'kb':   
        bw_size=2 ** 10
    if bw_unit== 'kB':   
        bw_size=2 ** 10 * 8
    if bw_unit== 'Tb':   
        bw_size=2 ** 40
    if bw_unit== 'TB':   
        bw_size=2 ** 40 * 8
    if bw_unit== 'Gb':
        bw_size=2 ** 30
    if bw_unit== 'GB':   
        bw_size=2 ** 30 * 8
    if bw_unit== 'Mb':   
        bw_size=2 ** 20
    if bw_unit== 'MB':    
        bw_size=2 ** 20 * 8  
    file_siz=file_size*file   
    bw_siz=bw_size*bw
    time= (1.0*file_siz)/bw_siz
    return convert_seconds(time)



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#0 hours, 37 minutes, 32.8 seconds