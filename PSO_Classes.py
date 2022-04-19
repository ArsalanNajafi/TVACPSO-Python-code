# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:22:30 2022

@author: Arsal
"""


"""
Created on Thu Apr  7 16:04:33 2022

@author: Arsalan
"""

import numpy as np
import random


def parameter():
    Nparticle = 200
    NIter = 100
    Dimension = 10
    return Nparticle, NIter, Dimension

[Nparticle, NIter, Dimension] = parameter()
MinBounds = -10
MaxBounds = 10
c1i = 2.5
c1f = 0.5
c2i = 0.5
c2f = 0.6

A = np.zeros([Nparticle,Dimension])
B = np.zeros([1,Nparticle])


#%%
# Class for allocating attributes of position, velocity, function value, and best values to each particle
class Particle:
                    
    def __init__(self):    
        self.Pos = np.zeros([1, Dimension])
        self.Velocity = np.zeros([1,Dimension])
        self.f = np.zeros([1])
        self.PBestValue = self.f
        self.PBest = self.Pos
 

#%%
# Second class for collectong all particles (objects) in set of a new object (population)
# Global best values are the attributes of object SearchSpace in class Population       
class Popoulation:
    def __init__(self, Nparticle,PBestS,PBestValueS, GBest, GBestValue):
        self.Nparticle = Nparticle
        self.GBestValue = GBestValue
        self.GBest = GBest
        self.PBestS = PBestS
        self.PBestValueS = 100000000*np.ones([Nparticle,1])

#%% Initial values of particles
    def Initialization(self):
        for particle in self.AllParticles:  
            for j in range(Dimension):
                particle.Pos[0,j] = MinBounds + random.random()*(MaxBounds - MinBounds)
            particle.PBest = particle.Pos

#%% Fitness function \sigma x^2    
    def FitnessFunction(self):  
        for particle in self.AllParticles:
            s = 0
            for j in range(Dimension):
                s += particle.Pos[0,j]**2 
            particle.f = s 
            
#%% Public best function
    def BestSelect(self):
        i = -1
        for particle in self.AllParticles:
            i += 1
            if particle.f<particle.PBestValue:
               particle.PBestValue = particle.f
               particle.PBest = particle.Pos
            A[i] = particle.PBest 
            B[0,i] = particle.PBestValue
        self.PBestS = A
        self.PBestValueS = B
        
#%% Global best function
    def GBestSelect(self):
        index = np.argmin(self.PBestValueS)
        self.GBest = self.PBestS[index]
        self.GBestValue = self.PBestValueS[0,index]
    
#%% Updating particles        
    def recom(self,k):
        for particle in self.AllParticles:
            c1 = c1i +  (c1f - c1i)*k/NIter
            c2 = c2i +  (c2f - c2i)*k/NIter
            omega = 0.5
            for j in range(Dimension):
                r1 = random.random()
                r2 = random.random()
                particle.Velocity[0,j] = omega*particle.Velocity[0,j] +  c1*r1*(particle.PBest[0,j] - particle.Pos[0,j]) +  c2*r2*(self.GBest[j] - particle.Pos[0,j])
                particle.Pos[0,j] = particle.Pos[0,j] + particle.Velocity[0,j] 

#%% Constraint handling of new particles (one population)               
    def ConsHand(self):
        for particle in self.AllParticles:
            for j in range(Dimension):
                if particle.Pos[0,j]<MinBounds:
                    particle.Pos[0,j] = MinBounds
                elif particle.Pos[0,j]>MaxBounds:
                     particle.Pos[0,j] = MaxBounds

 

    
