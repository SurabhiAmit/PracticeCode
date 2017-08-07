#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    first,second=0,1
    for i in range(0,n):
        first,second = second,first+second
    return first    
    

print fibonacci(36)
#>>> 14930352