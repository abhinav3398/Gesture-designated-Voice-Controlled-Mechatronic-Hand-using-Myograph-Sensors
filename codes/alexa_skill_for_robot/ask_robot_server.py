# Project Name:	gesture controled & voice designated robotic hand using myograph sensors
# Author List:		Abhinav Lakhani
# file name:		ask_robot_server.py
# Functions:		new_robot(), hand_close(), hand_open(), gesture_start(), gesture_stop(), session_ended(), stopintent(), cancelintent()
# Global Variables:app, ask

import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

#* initialize flask instance
app = Flask(__name__)
#* initialize alexa skill
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)## initialize data logging

@ask.launch
def new_rebot():
    '''
    Function Name:  new_robot()
    Input:          alexa launch skill instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"1,0,1"
                    & then close the text file.
                    after that tell alexa to greet the user by obtaining the welcome message obtained from templates.yaml file,
                    and ask the user to for next command.
    Example:        alexa start robot
    '''
    welcome_msg = render_template('welcome')
    file = open("message.txt", "w")
    file.write((str(0) + ',' + str(0) + ',' + str(1)))#argument must be a string
    file.close()
    return question(welcome_msg)

@ask.intent("CloseIntent")
def hand_close():
    '''
    Function Name:  hand_close()
    Input:          alexa "CloseIntent" instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"1,0,1"
                    & then close the text file.
                    after that tell alexa to inform the user that the hand has been closed,
                    by obtaining the "closed" message from templates.yaml file,
                    and ask the user to for next command.
    Example:        alexa start robot and grab
    '''
    file = open("message.txt", "w")
    file.write((str(1) + ',' + str(0) + ',' + str(1)))#argument must be a string 
    file.close()
    close_msg = render_template('closed')    
    return question(close_msg)

@ask.intent("OpenIntent")
def hand_open():
    '''
    Function Name:  hand_open()
    Input:          alexa "OpenIntent" instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"0,0,1"
                    & then close the text file.
                    after that tell alexa to inform the user that the hand has been copened,
                    by obtaining the "opened" message from templates.yaml file,
                    and ask the user to for next command.
    Example:        alexa start robot and release
    '''
    file = open("message.txt", "w")
    file.write((str(0) + ',' + str(0) + ',' + str(1)))#argument must be a string
    file.close()
    open_msg = render_template('opened')    
    return question(open_msg)
    
@ask.intent("GestureStartIntent")
def gesture_start():
    '''
    Function Name:  gesture_start()
    Input:          alexa "GestureStartIntent" instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"0,1,1"
                    & then close the text file.
                    after that tell alexa to inform the user that the gesture recognition has been started,
                    by obtaining the "gesture_start_msgd" message from templates.yaml file;
                    and ask the user to for next command.
    Example:        alexa start robot and gesture on
    '''
    file = open("message.txt", "w")
    file.write((str(0) + ',' + str(1) + ',' + str(1)))#argument must be a string
    file.close()
    gesture_start_msg = render_template('gesture_start_msg')        
    return question(gesture_start_msg)
    
@ask.intent("GestureStopIntent")
def gesture_stop():
    '''
    Function Name:  gesture_stop()
    Input:          alexa "GestureStopIntent" instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"0,0,1"
                    & then close the text file.
                    after that tell alexa to inform the user that the gesture recognition has been stopped,
                    by obtaining the "gesture_stop_msgd" message from templates.yaml file;
                    and ask the user to for next command.
    Example:        alexa start robot and gesture off
    '''
    file = open("message.txt", "w")
    file.write((str(0) + ',' + str(0) + ',' + str(1)))#argument must be a string
    file.close()
    gesture_stop_msg = render_template('gesture_stop_msg')            
    return question(gesture_stop_msg)

@ask.session_ended
def session_ended():
    '''
    Function Name:  session_ended()
    Input:          alexa session ended instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"0,0,0"
                    & then close the text file.
                    after that tell alexa to exit the skill,
                    by obtaining the "goodbye" message from templates.yaml file,
                    & displaying it to the user.                    
    Example:        none
    '''
    file = open("message.txt", "w")
    file.write((str(0) + ',' + str(0) + ',' + str(0)))#argument must be a string
    file.close()
    sess_ended_msg = render_template('goodbye')                
    return statement(sess_ended_msg)

@ask.intent("AMAZON.CancelIntent")
def cancelintent():
    '''
    Function Name:  cancelintent()
    Input:          alexa session ended instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"0,0,0"
                    & then close the text file.
                    after that tell alexa to exit the skill,
                    by obtaining the "goodbye" message from templates.yaml file,
                    & displaying it to the user.                    
    Example:        none
    '''
    file = open("message.txt", "w")
    file.write((str(0) + ',' + str(0) + ',' + str(0)))#argument must be a string
    file.close()
    sess_ended_msg = render_template('goodbye')                
    return statement(sess_ended_msg)
    
@ask.intent("AMAZON.StopIntent")
def stopintent():
    '''
    Function Name:  stopintent()
    Input:          alexa session ended instance
    Output:         a template file containing sentences(speakable) which alexa can speak.
    Logic:          open a text file(in write mode) & write into it string"0,0,0"
                    & then close the text file.
                    after that tell alexa to exit the skill,
                    by obtaining the "goodbye" message from templates.yaml file,
                    & displaying it to the user.                    
    Example:        none
    '''
    file = open("message.txt", "w")
    file.write((str(0) + ',' + str(0) + ',' + str(0)))#argument must be a string
    file.close()
    return statement("Thank You for using Gesture designated & Voice controlled Mechatronic Hand using Electromyograph Sensor. Goodye!")

#* start skill
if __name__ == '__main__':
    app.run(debug=True)
    
#! after this to attach this to the server add this line with the port provided by 
#! the server buidt by this code
#! sudo ./ngrok http 5000