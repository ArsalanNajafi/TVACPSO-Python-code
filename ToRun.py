# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 19:31:25 2022

@author: Arsalan Najafi
Time Varying Particle Swarom Optimization code

This file should be run connected to classes file.
"""


import numpy as np
from PSO_Classes import Particle
from PSO_Classes import Popoulation
import matplotlib.pyplot as plt
from PSO_Classes import parameter

[Nparticle, NIter, Dimension] = parameter()

#%% Initia zero and big number matrices
PBestValueS = 100000000*np.ones([Nparticle,1])
GBest = np.zeros([1,Dimension])
PBest = np.zeros([1,Dimension])
GBestValue = []
PBestS = np.zeros([Nparticle,Dimension])

#%% Defining SearchSpace as the objective of class population
# and  collecting the object particle from the previous class into the new object set AllParticles
SearchSpace =  Popoulation(Nparticle,PBestS,PBestValueS, GBest, GBestValue)   
Aux = [Particle() for _ in range(SearchSpace.Nparticle)]
SearchSpace.AllParticles = Aux

#%% Iterative algorithm
Out = np.zeros(NIter)
SearchSpace.Initialization()
SearchSpace.FitnessFunction()
for particle in SearchSpace.AllParticles:
    particle.PBestValue = particle.f
    
SearchSpace.BestSelect()
SearchSpace.GBestSelect()
for k in range(NIter):
    SearchSpace.recom(k)
    SearchSpace.ConsHand()
    SearchSpace.FitnessFunction()
    SearchSpace.BestSelect()
    SearchSpace.GBestSelect()   
    Out[k] = SearchSpace.GBestValue
    
print('Optimal fitness =\n', SearchSpace.GBestValue) 
print('\n')    
print('Best soution =\n',SearchSpace.GBest) 

#%% drawing convergence figure
plt.figure(1)
x =np.arange(1,NIter+1,1)
plt.plot(x,Out)
plt.xlabel('Iteration')
plt.ylabel('Objective function')
plt.show()