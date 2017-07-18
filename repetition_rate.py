#Define a procedure that outputs a dictionary with the repetition rate of each element of the input list.

def repetition_rate(p):
    if len(p)==0:
        return None
    best=p[0]
    count=1
    counts={}
    for i in range(1,len(p)):
        if p[i]==best:
            count+=1
        if p[i]!=best:
            print best,p[i]
            if best not in counts:
                counts[best]=count
            if best in counts:
                if counts[best] < count:
                    counts[best]=count
            counts[best]=count
            best=p[i]
            count=1
        if i==len(p)-1:
            if p[i] not in counts:
                counts[p[i]]=count
            if p[i] in counts:
                if counts[p[i]] < count:
                    counts[p[i]]=count
    return counts      
    