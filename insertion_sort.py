# insertion sort implemented in python

def insertion_sort(input):
    for i in range(1,len(input)):
        value=input[i]
        j=i
        while j>0 and input[j-1]>value:
            input[j]=input[j-1]
            j-=1
        input[j]=value    
    return input            
                
print insertion_sort([1,8,5,4,3,2])    