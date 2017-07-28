#selection sort implemented in python

def selection_sort(input):
    for i in range(len(input)-1):
        for j in range(i+1,len(input)):
            if input[i]>input[j]:
                input[i],input[j]=input[j],input[i]
    return input