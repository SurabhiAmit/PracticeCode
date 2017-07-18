# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(p):
    if not p:
        return None
    best,best_count,prev,count=p[0],1,p[0],1
    for i in range(1,len(p)):
        current=p[i]
        if current==best:
            best_count+=1
        if current==prev:
            count=count+1
        else:
            count=1
        if count > best_count:
            best_count=count
            best=current
        prev=current
    return best  
        




#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

