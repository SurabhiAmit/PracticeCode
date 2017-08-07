#bubble sort implemented in python

def bubble_sort(input):
    for k in range(1,len(input)-1):
        for i in range(0,len(input)-k):
            if input[i+1]<input[i]:
                input[i+1],input[i]=input[i],input[i+1]
    return input            
                
print bubble_sort([1,8,5,4,3,2])      