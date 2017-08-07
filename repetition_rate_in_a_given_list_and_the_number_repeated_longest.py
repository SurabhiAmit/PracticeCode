# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def repetition_rate(p):
    result,prev,count=[],p[0],1
    for i in range(1,len(p)):
        if p[i]==prev:
            count+=1
        else:
            result.append([prev,count])
            prev=p[i]
            count=1
        if i==len(p)-1:
            result.append([prev,count])
    return result
    
#to output the element in input list that repeated most consecutively first.
def longest_repetition(p):
    if len(p)==0:
        return None
    if len(p)==1:
        return p[0]
    result=repetition_rate(p)
    n=len(result)-1
    best=result[n][0]
    best_count=result[n][1]
    for i in range(n,-1,-1):
        if result[i][1]>=best_count:
            best=result[i][0]
            best_count=result[i][1]
    return best        
            



#For example,

p=[1,2,2,3,3,3,2,2,2]    
print repetition_rate(p)
#[[1, 1], [2, 2], [3, 3], [2, 3]]   
print longest_repetition(p)
#3

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

