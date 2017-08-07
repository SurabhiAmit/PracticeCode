def merge_sort(input):
    if len(input)<2:
        return input
    middle=int(len(input)/2)
    a=input[0:middle]
    b=input[middle:]
    left=merge_sort(a)
    right=merge_sort(b)
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if k<len(input):
            if left[i]<right[j]:
                input[k]=left[i]
                i+=1
                k+=1
            else:
                input[k]=right[j]
                j+=1
                k+=1
    while i<len(left):
        input[k]=left[i]
        i+=1
        k+=1
    while j<len(right) :
        input[k]=right[j]
        j+=1
        k+=1 
    return input    
    
print merge_sort([1,9,5,3,8,0,2,1])    
    
