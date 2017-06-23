# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(s,t):
    l=len(s)
    rev=s[::-1]
    if t=="":
    	return l
    if s.find(t)!=-1:
        a=l-rev.find(t)-1
        return a 
    return -1  
    
print find_last("222222222", "")