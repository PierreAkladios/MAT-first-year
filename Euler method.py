#Author: Pierre Akladios
def Euler(x,y,h,target):
    '''
    change f depending on the case
    (num,num,num,num)->num
    x et y initial
    h= hop
    t=quand arreter
    '''
    while(x<target):
        f=(0.2*x)+(0.2*y)##change depending on question
        y=y+h*f
        x=x+h
    return y


