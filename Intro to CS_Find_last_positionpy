# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.
#new commit
def find_last(s,t):
	if t=="":
		return len(s)
	if s.find(t)!=-1:
		n=0
		while s.find(t)!=-1:
			pos=s.find(t)
			n=n+pos+1
			s=s[pos+1:]
			return n-1
	return -1
    
print find_last("222222222", "")
print find_last('udacity','kite')
print find_last('asdasda','a')