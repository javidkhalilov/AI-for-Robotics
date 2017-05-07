# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:08:14 2016

@author: Javid
"""

from matrix import matrix
from robot import robot

#x=matrix([[bot.x],[bot.y],[3.],[4.]])
#print(x)

#def estimate(xi,yi,other=None):
#    est_pose=matrix([[xi],[yi],[0.1],[0.2]])
#    return est_pose
#    
#print(estimate(bot.x,bot.y))

def estimate_next_pose(measurements,xi,yi):
    
    dt=0.1
    
    x=matrix([[xi],[yi],[0.],[0]]) 
    u = matrix([[0.], [0.], [0.], [0.]]) # external motion

    #### DO NOT MODIFY ANYTHING ABOVE HERE ####
    #### fill this in, remember to use the matrix() function!: ####

    # initial uncertainty: 0 for positions x and y, 1000 for the two velocities
    P =  matrix([[0., 0.,0.,0], [0., 0.,0.,0.],[0., 0.,1000.,0.],[0., 0.,0.,1000.]]) 
    # next state function: generalize the 2d version to 4d
    F =  matrix([[1., 0.,dt,0.],[0., 1.,0.,dt],[0., 0.,1.,0.],[0., 0.,0.,1.]])
    # measurement function: reflect the fact that we observe x and y but not the two velocities
    H =  matrix([[1.,0.,0.,0.],[0.,1.,0.,0.]])
    # measurement uncertainty: use 2x2 matrix with 0.1 as main diagonal
    R =  matrix([[0.1, 0.], [0., 0.1]])
    # 4d identity matrix
    I =  matrix([[1., 0.,0.,0.], [0., 1.,0.,0.],[0., 0.,1.,0.],[0., 0.,0.,1.]])
#
    for n in range(len(measurements)):
        
        x = (F * x) + u
#        P = F * P * F.transpose()
#        
        # measurement update
#        Z = matrix([measurements[n]])
#        y = Z.transpose() - (H * x)
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()
#        x = x + (K * y)
#        P = (I - (K * H)) * P
        xy_estimate=x    
#    xy_estimate=x
    
    return xy_estimate
    
bot=robot(0.1,2.1,0.,0.,0.)
measurements=bot.sense()
    
print(estimate_next_pose(measurements,bot.x,bot.y))