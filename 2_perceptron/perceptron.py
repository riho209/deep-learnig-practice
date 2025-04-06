import numpy as np

def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    num=w1*x1+x2*w2
    if num<=theta:
        y=0
    else:
        y=1
    
    return y

if __name__ == '__main__':
    x1,x2=map(float,input().split())
    print('AND:',AND(x1,x2))