
# To print count number of random integers between the limits passed in 

def randomintegers(a,b,count):
    if count >(b-a +1):
        return 'Invalid' 
    num,checked,first=0,[],a
    while num< (count/2) and a<b:
        if (a+b) %2 ==0:
            c=(a+b)/2
            #if c not in checked:
            print c
            checked.append((a+b)/2)
            num+=1
            a+=1
        else:
            c= (a+b-1)/2
            #if c not in checked:
            print c
            checked.append((a+b-1)/2) 
            num+=1
            a+=1
    while num<count and b>0:
        a=first
        if (a+b) %2 ==0:
            c=(a+b)/2
            #if c not in checked:
            print c
            checked.append((a+b)/2)
            num+=1
            b-=1
        else:
            c= (a+b-1)/2
            #if c not in checked:
            print c
            checked.append((a+b-1)/2) 
            num+=1
            b-=1
            
                
                
print randomintegers(1,100,100)