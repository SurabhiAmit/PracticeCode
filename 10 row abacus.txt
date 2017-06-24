#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.


def print_abacus(value):
    s,i,k=str(value),10,0
    if i<len(s):
        print'Too big to be displayed on 10 row abacus'
        return
    while i>len(s):
        print '|'+('0' *5)+ ('*' *5 )+'   '+'|'
        i-=1
    while (k<len(s)):
        if int(s[k]) <=5:
            print '|'+'0'*5 +'*' *(5-int(s[k]))+'   '+'*'* int(s[k])+'|'
        else:
            print '|'+'0'*(10-int(s[k]))+'   '+'0'*(int(s[k])-5)+'*'*5+'|'
        k+=1
    
    
    
       

###  TEST CASES..Expected output
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|

 Output
 ======
 
 Abacus showing 0:
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
Abacus showing 12345678:
|00000*****   |
|00000*****   |
|00000****   *|
|00000***   **|
|00000**   ***|
|00000*   ****|
|00000   *****|
|0000   0*****|
|000   00*****|
|00   000*****|
Abacus showing 1337:
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000*****   |
|00000****   *|
|00000**   ***|
|00000**   ***|
|000   00*****|