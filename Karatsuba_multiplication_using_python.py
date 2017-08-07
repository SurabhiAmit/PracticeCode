Karatsuba_multiplication_using_python

def multiply(x,y):
    first,second=str(x),str(y)
    if len(first) <= 2 or len(second) <= 2:
        return x*y
    med_x=len(first)/2
    #print med_x
    a_x=first[:med_x]
    b_x=first[med_x:]
    m,l=len(b_x),len(second)
    c_y=second[:l-m]
    d_y=second[l-m:]
    a,b,c,d=int(a_x),int(b_x),int(c_y),int(d_y)
    step1=multiply(a,c)
    step2=multiply(b,d)
    step3=multiply((a+b),(c+d))
    step4=step3-step2-step1
    #print step1,step2,step3,step4
    result=(step1)*(10**(2*m))+step2+(step4)*(10**m)
    return result
    
print multiply (3141592653589793238462643383279502884197169399375105820974944592

,2718281828459045235360287471352662497757247093699959574966967627)   
#>>853973422267356706546355086954657449503488853576511496187960112706774
#3044893204848617875072216249073013374895871952806582723184    
    