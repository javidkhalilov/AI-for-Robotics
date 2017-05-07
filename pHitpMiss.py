# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:58:12 2016

@author: Javid
"""

p=[0.2,0.2,0.2,0.2,0.2]
#p=[0,1,0,0,0]
world=['green', 'red', 'red', 'green', 'green']
Z = 'green'
measurements=['red','red']
motions=[1,1]
pHit = 0.6
pMiss = 0.2
Sum=0.0

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
#Enter code here
#p[0]=p[0]*pMiss
#p[1]=p[1]*pHit
#p[2]=p[2]*pHit
#p[3]=p[3]*pMiss
#p[4]=p[4]*pMiss

#print(p)
#print(sum(p))
#
#for i in range(5):
#    Sum+=p[i]
#
#print(Sum)

def sense(p,Z):
    q=[]
    for j in range(len(p)):
#        if world[j]==Z:
#            q.append(p[j]*pHit)
#        else:
#            q.append(p[j]*pMiss)
        hit=(Z==world[j])
        q.append(p[j]*(hit*pHit+(1-hit)*pMiss))
        
    s=sum(q)
    for i in range(len(p)):
            q[i]=q[i]/s        
    return q
    
#for i in range(len(measurements)):
#    p=sense(p,measurements[i])
#    
#print(p)
    
def move(p,U):
    q=[]
    for k in range(len(p)):
        s=pExact*p[(k-U)%len(p)]
        s=s+pOvershoot*p[(k-U-1)%len(p)]
        s=s+pUndershoot*p[(k-U+1)%len(p)]
        q.append(s)
    return q
    
for i in range(len(measurements)):
    p=sense(p,measurements[i])
    p=move(p,motions[i])

print(p)
