# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    if ord(letter)+n > 122:
        return chr(96+(ord(letter)+n-122))
    if ord(letter)+n < 97:
        return chr(123-(97-(ord(letter)+n)))
    return chr(ord(letter)+n)
    
def rotate(name,n):
    i,output=0,''
    while i<len(name):
        if name[i]!=" ":
            output+=shift_n_letters(name[i],n)
        else:
            output+=" "
        i+=1
    return output    
            
            
    

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)