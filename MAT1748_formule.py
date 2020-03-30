#Author: Pierre Akladios

#Operations on sets
#and: a&b
#or: a|b
#xor: a^b
def P(n,r):
    """
    (int,int)->int
    Permutation
    precondition n et r sont positif r est plus perit que n
    """
    return (factorial(n)/factorial(n-r))

def C(n,r):
    """
    (int,int)->int
    combinaison
    precondition n et r sont positif et r est plus perit que n
    """
    return (factorial(n)/(factorial(r)*factorial(n-r)))

def factorial(n):
    """
    (int)->int
    factorial
    precondition n est positif
    """
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
    
    
