## Project Name:	gesture controled & voice designated robotic hand using myograph sensors
## Author List:		Abhinav Lakhani
## file name:		emg_datacapture.py
## Functions:		np, Arduino, util
## Global Variables:file, it, a, b, flagindex, readings
#? import python serial library for controlling arduino 
from pyfirmata import Arduino, util
#? import numpy for data processing
import numpy as np
#* initialize which arduino used & port used
#board = Arduino('/dev/ttyUSB0')
board = Arduino('/dev/ttyACM0')
#! remember to exit the arduino when done using it.
#! by running below line(uncomment first) after done working.
#! board.exit()
#? open a text file for writing only
file = open("emg_entries.txt", "w")
#* check if the board is working by,
#* blinking inbuilt leds at the start of the code
board.digital[13].write(1)
board.digital[13].write(0)
#* start iterstor for capturing analog readings
it = util.Iterator(board)
it.start()
#* no. of emg signals/samples (i.e sampling frequency)
f=20
#* matrix to process a sample waveforms
a = np.mat(np.zeros((f,), dtype=np.float))
b = np.mat(np.zeros((f,), dtype=np.float))
#* flags: for the user to when(at which time) to flex the arm, or to release it
flag = np.mat(np.zeros((3050,), dtype=np.float))
flag[0,1150:1200]=1
flag[0,1250:1300]=1
flag[0,1400:1450]=1
flag[0,1550:1600]=1
flag[0,1700:1800]=1
flag[0,1850:1950]=1
flag[0,2050:2150]=1
flag[0,2300:2450]=1
flag[0,2500:2650]=1
flag[0,2800:2950]=1
#* enable analog analog
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
index = 0x01
readings = 3050
while(index < readings):
	#* capture analog
	t0 = board.analog[0].read()
	t1 = board.analog[1].read()
	## if analog values are NULL then zero
	if (t0 == None or t1 == None):
            t0 = 0
			t1 = 0
	#* update the matrix
	a = np.concatenate((a[0, 1:], np.mat(t0)), axis=1)
	b = np.concatenate((b[0, 1:], np.mat(t1)), axis=1)
	## RMS value of signal
	RMS1 = np.sqrt(np.sum(np.power(a, 2))/f)
	RMS1 = np.sqrt(np.sum(np.power(b, 2))/f)
	## mean of signal
	MEAN1 = np.mean(a)
	MEAN2 = np.mean(b)
	if (RMS1 > 0.32 or RMS1 < 0.305 or RMS2 > 0.32 or RMS2 < 0.305):
        index = 1
    else:
        index = 0	
	#* write to the opened text file in matlab matrix format
	file.write((str(t0) + ',' + str(t1) + ',' + str(RMS1) +  ',' +str(RMS2) +  ',' +str(MEAN1) +  ',' +str(MEAN2) + ',' + str(index)))#argument must be a string		
	file.write('\n')#new line in text file
	#* print the values & reading number & flag to user
	##if (index % 5 == 0):
	##	print(str(t0) + '; ' + '''str(t1)''' + '; ' + str(RMS) + '; ' + str(MEAN) + '; ' + str(flag[0,index]))
	print(str(flag[0,index+10]) + '; ' + str(index))
	index += 1
	#* delay for board
	board.pass_time(.001)