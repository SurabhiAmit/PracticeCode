# Write a program to sort a list of numbers provided on standard input 
# (for instance, the numbers you generated above). 
# You are NOT allowed to call external routines to do the sorting for you. 
# After sorting the numbers, print them out. Focus on a simple method (not an efficient method).

def sort(numbers):
    l=len(numbers)
    for i in range(l):
        for j in range(i,l):
            if numbers[j] <numbers[i]:
                numbers[i],numbers[j]=numbers[j],numbers[i]
    return numbers
print sort([3,2,4,7,6,0])