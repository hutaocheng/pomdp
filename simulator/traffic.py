#-*- encoding:utf-8 -*-
from environment import  Discrete
if __name__== "__main__":
    #user level state related to conception mileage and lane of road, gear of auto   
    mileage, lane, gear = 32, 4, 5
    
    #initialize system with pomdp model 
    nState, nAction = (mileage, lane, gear), 5
    environ = Discrete(nState, nAction)
    print('pomdp based environment estiblished')
