import numpy as np

def AND(x1,x2):
    #重みとバイアス
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    num=np.sum(w*x)+b
    if num<=0:
        y=0
    else:
        y=1
    
    return y

if __name__ == '__main__':
    x1,x2=map(float,input().split())
    print('AND:',AND(x1,x2))