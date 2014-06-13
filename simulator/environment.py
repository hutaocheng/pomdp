#-*- encoding:utf-8 -*-
import numpy
from numpy import random

class Environment(object):
    """enviroment interactive with agent.
       there are three objects related with the topic: environment, agents, and problem solver.
       general speaking, solving problem with environment directly is difficult, but we can learn
       problem solver based on interactive between agents and environment. pomdp is the model
       describing transaction M=(s,a,x,t,o,\gamma,r) where,
       *   s(static) and t(dynamic) owned by environment, 
       ** a(static) owned by agents
       ***x(static), o, \gamma and r owned or trigged by interaction.
    """
    
    def __init__(self):
        """system is pomdp based 
        """
        pass
        
       
    def interactive(self, action):
        """agent action->enviroment feedback,which could be observation powered by physics engin.
        """
        pass
        
#

class Discrete(Environment):    
    """discrete  pomdp model.
    """
    def __init__(self, nState, nAction, gamma=0.9, dObservation=0):
        self.nState, self.nAction, self.dObservation = numpy.array((nState, ) if isinstance(nState, int) else nState), numpy.array((nAction, ) if isinstance(nAction, int) else nAction), dObservation 
        
        #transition model
        self.t = numpy.zeros(list(self.nState)+list(self.nAction)+list(self.nState))
        self.t = self.t.reshape(self.nState.prod(),self.nAction.prod(), self.nState.prod())
        #reward
        self.gamma = gamma
        self.r = numpy.zeros((self.nState.prod(), self.nAction.prod()))
        #factorized based observation model
        if dObservation != 0:
            self.o = numpy.zeros(list(self.nState)+list(self.nAction)+(self.dObservation, ))
            self.o = self.o.reshape(self.nState.prod(), self.nAction.prod(), -1)

    
    def recurvision(self, St):
        if len(St) == 1:
            return St
        else:
            return St[0]*recurse(self, St[1:])
            
     
    def interaction(self, action):
        pass
        

class Continuous(Environment):
    """continuous podmp model.
       there are two type integration method for different dimension variable:
       *  structured prediction which ross did works on(it is a bit complicated than later method),
       **deep neural networks which is based on decomposition of graph. 
    """
    def __init__(self, dState, dAction, gamma=0.9, dObservation=0):
        self.dState, self.dAction, self.dObservation = dState, dAction, dObservation 
        #transition model
        self.t = numpy.zeros((self.dState, self.dAction, self.dState))
        #reward
        self.gamma = gamma
        self.r = numpy.zeros((self.dState, self.dAction))
        #factorized based observation model
        if dObservation != 0:
            self.o = numpy.zeros((self.dState, self.dAction, self.dObservation))
