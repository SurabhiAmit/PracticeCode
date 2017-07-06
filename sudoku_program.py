# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]
        

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
               ###############################################
               
def check_sudoku(p):
    n,length=0,len(p[0])
    list_length,k=len(p),0   #defensive programming
    while k<list_length:
        if len(p[k])!=list_length:
            return False
        k+=1
    while n<length:
        i=n+1
        while i<length:
            for e in p:
                if e[n]==e[i] or not isinstance (e[n],int):
                    return False
            i=i+1
        n=n+1  
    k=0
    while k<length:
        n=0
        while n<length:
            i=n+1
            while i<length:
                if p[n][k]==p[i][k] or not isinstance(p[n][k],int):
                    return False
                i=i+1
            n=n+1 
        k+=1 
    q=0
    while q<length:
        n=length
        while n>0:
            if n not in p[q]:
                return False
            n=n-1
        q=q+1 
    return True  
    
                ###############################################
    
    
    #to check if all elements are whole numbers
    #def isnumber(a):
    #    return isinstance(a,int)
    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False


