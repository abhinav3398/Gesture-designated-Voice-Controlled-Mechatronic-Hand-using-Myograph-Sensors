## Project Name:	gesture controled & voice designated robotic hand using myograph sensors
## Author List:		Abhinav Lakhani
## file name:		lib.py
## Functions:		np, Arduino, util, sp, sys, time, sigmoid, predict, (class)stepper, (class)stepper, busio, 
## Global Variables:theta

#* import libraries
from pyfirmata import Arduino, util
import numpy as np
import scipy as sp
import sys
import time
#* import adafruit capacitive sensor library for touch
import board as bd
import busio
#* Import MPR121 module.
import adafruit_mpr121

#? theta obtained by machine learning on matlab
theta = np.array([[-9.031172],
                  [-6.242038],
                  [-4.617360],
                  [-2.577350],
                  [-0.318678],
                  [0.994083],
                  [1.637086],
                  [-7.292429],
                  [0.062445],
                  [0.581523],
                  [2.915947],
                  [3.535023],
                  [5.408421],
                  [6.366676],
                  [7.599101],
                  [-0.457920]])

def sigmoid(z):    
    '''
    Function Name:  sigmoid(z)
    Input:          numpy matrix(maximim 2 dimentions) containing numerical values only
    Output:         numpy matrix containing numerical values only
    Logic:          mathematical function: f(x) = 1 / (1 + epsilon^(-x))
    Example:        a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
                    b = sigmoid(a)
    '''
    g = np.zeros(np.shape(z))    
##    ? ====================== //// //// //// ======================
##    ? Instructions: Compute the sigmoid of each value of z (z can be a matrix,
##    ?               vector or scalar).    
    g = 1 / (1 + np.exp(-z))
    #print(g)
    return g

def predict(theta, X):
    '''
    Function Name:  predict(z)
    Input:          2 numpy matrices(maximim 2 dimentions) containing numerical values only
    Output:         numpy matrix containing numerical(1s or 0s only) values only
    Logic:          predicts the possibility of output from the inputs & theta parameter,
                    output 1 being High or True & 0 being Low or False
    Example:        X = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
                    theta = lib.theta
                    y = sigmoid(theta, X)    
    '''    
    m = X.shape[0]
    theta = theta.transpose()
##    * need to return the following variables correctly
    p = np.zeros((m, 1))
##    ? ====================== //// //// //// ======================
##    ? Instructions: to make predictions using
##    ?               your learned logistic regression parameters. 
##    ?               You should set p to a vector of 0's and 1's
    pre_sig = np.zeros((1,5))
    for i in range(m):
        #pre_sig[5] = pre_sig[4]
        pre_sig[0,4] = pre_sig[0,3]
        pre_sig[0,3] = pre_sig[0,2]
        pre_sig[0,2] = pre_sig[0,1]
        pre_sig[0,1] = pre_sig[0,0]
        pre_sig[0,0] = sigmoid(sp.matmul(theta,X[i,:].transpose()))
        #print(pre_sig)
        if ((pre_sig[0,0] >= 0.44 or pre_sig[0, 0] <= 0.36)):
            p[i] = 1
        else:
            p[i] = 0        
    return p

#'''
class stepper(object):
    '''
    Function Name:  (class) stepper
    Input:          first parameter should be instance containing of aduino board,
                    followed by the 3 pin number pairs(pairs of four) each containing the pins used by their individual stepper
    Output:         functions
    Logic:          stepper class for 3 stepper motor operation
    Example:        boarda = Arduino('/dev/ttyACM0')
                    stepper_a = stepper(boarda, stepper1_pin1, stepper1_pin2, stepper1_pin3, stepper1_pin4,
                                            stepper2_pin1, stepper2_pin2, stepper2_pin3, stepper2_pin4,
                                            stepper3_pin1, stepper3_pin2, stepper3_pin3, stepper3_pin4)
    '''
    def __init__(self, board, pina1, pinb1, pinc1, pind1, pina2, pinb2, pinc2, pind2, pina3, pinb3, pinc3, pind3):
        '''
        Function Name:  stepper.__init__
        Input:          stepper class object
        Output:         None
        Logic:          Stepper motor initialization as defined in the description        
        '''
        #initialize board
        self.board = board
        #for stepper 1
        self.pinA1 = pina1
        self.pinB1 = pinb1
        self.pinC1 = pinc1
        self.pinD1 = pind1
        #for stepper 2
        self.pinA2 = pina2
        self.pinB2 = pinb2
        self.pinC2 = pinc2
        self.pinD2 = pind2
        #for stepper 3
        self.pinA3 = pina3
        self.pinB3 = pinb3
        self.pinC3 = pinc3
        self.pinD3 = pind3

    def step(self, delay = 0.05, step = 1):
        '''
        Function Name:  stepper.step
        Input:          first parameter should be the delay between each individual step taken(in seconds),
                        second parameter should be the number(integer) of steps taken.
        Output:         None
        Logic:          each four stepper motors are rotated as the steps & delay being specified
        Example:        stepper_a.step(0.001, -1)
        '''
        if (step > 0):
            while(step > 0):
                self.board.digital[self.pinD1].write(1);self.board.digital[self.pinC1].write(0);self.board.digital[self.pinB1].write(0);self.board.digital[self.pinA1].write(1)
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay)
                self.board.digital[self.pinD1].write(1);self.board.digital[self.pinC1].write(0);self.board.digital[self.pinB1].write(1);self.board.digital[self.pinA1].write(0)
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD1].write(0);self.board.digital[self.pinC1].write(1);self.board.digital[self.pinB1].write(1);self.board.digital[self.pinA1].write(0)
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD1].write(0);self.board.digital[self.pinC1].write(1);self.board.digital[self.pinB1].write(0);self.board.digital[self.pinA1].write(1)
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay)
                step -= 1
        elif (step < 0):
            while(step < 0):
                self.board.digital[self.pinD1].write(0);self.board.digital[self.pinC1].write(1);self.board.digital[self.pinB1].write(0);self.board.digital[self.pinA1].write(1)
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay)
                self.board.digital[self.pinD1].write(0);self.board.digital[self.pinC1].write(1);self.board.digital[self.pinB1].write(1);self.board.digital[self.pinA1].write(0)
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD1].write(1);self.board.digital[self.pinC1].write(0);self.board.digital[self.pinB1].write(1);self.board.digital[self.pinA1].write(0)
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD1].write(1);self.board.digital[self.pinC1].write(0);self.board.digital[self.pinB1].write(0);self.board.digital[self.pinA1].write(1)
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay)
                step += 1
#'''

class stepper2(object):
    '''
    Function Name:  (class) stepper2
    Input:          first parameter should be instance containing of aduino board,
                    followed by the 2 pin number pairs(pairs of four) each containing the pins used by their individual stepper
    Output:         functions
    Logic:          stepper class for 2 stepper motor operation
    Example:        boarda = Arduino('/dev/ttyACM0')
                    stepper_a = stepper(boarda, stepper1_pin1, stepper1_pin2, stepper1_pin3, stepper1_pin4,
                                            stepper2_pin1, stepper2_pin2, stepper2_pin3, stepper2_pin4)
    '''
    def __init__(self, board, pina2, pinb2, pinc2, pind2, pina3, pinb3, pinc3, pind3):
        '''
        Function Name:  stepper.__init__
        Input:          stepper class object
        Output:         None
        Logic:          Stepper motor initialization as defined in the description 
        '''
        #initialize board
        self.board = board
        #for stepper 2
        self.pinA2 = pina2
        self.pinB2 = pinb2
        self.pinC2 = pinc2
        self.pinD2 = pind2
        #for stepper 3
        self.pinA3 = pina3
        self.pinB3 = pinb3
        self.pinC3 = pinc3
        self.pinD3 = pind3
    
    def step(self, delay = 0.05, step = 1):
        '''
        Function Name:  stepper.step
        Input:          first parameter should be the delay between each individual step taken(in seconds),
                        second parameter should be the number(integer) of steps taken.
        Output:         None
        Logic:          each four stepper motors are rotated as the steps & delay being specified
        Example:        stepper_a.step(0.001, -1)
        '''
        if (step > 0):
            while(step > 0):
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay) 
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay)
                step -= 1
        elif (step < 0):
            while(step < 0):
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay)
                self.board.digital[self.pinD2].write(0);self.board.digital[self.pinC2].write(1);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(0);self.board.digital[self.pinC3].write(1);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(1);self.board.digital[self.pinA2].write(0)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(1);self.board.digital[self.pinA3].write(0)
                self.board.pass_time(delay)
                self.board.digital[self.pinD2].write(1);self.board.digital[self.pinC2].write(0);self.board.digital[self.pinB2].write(0);self.board.digital[self.pinA2].write(1)
                self.board.digital[self.pinD3].write(1);self.board.digital[self.pinC3].write(0);self.board.digital[self.pinB3].write(0);self.board.digital[self.pinA3].write(1)
                self.board.pass_time(delay)
                step += 1
