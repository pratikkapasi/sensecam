import numpy as np
import cv2
import os, sys
from config import count
from config import emotion

# Emotions
	# 1: Anger
	# 2: Fear
	# 3: Disgust
	# 4: Contempt
	# 5: Joy
	# 6: Sadness
	# 7: Surprise

quality = '0'

while(quality!='1'):
	cap = cv2.VideoCapture(0)

	# Define the codec and create VideoWriter object
	#fourcc = cv2.VideoWriter_fourcc(*'XVID')
	fourcc=cv2.cv.CV_FOURCC('X','V','I', 'D')
	out = cv2.VideoWriter('videos/sample_'+str(count)+'_'+str(emotion)+'.avi',fourcc, 20.0, (640,480))
	t = 0

	while(cap.isOpened()):
	    ret, frame = cap.read()
	    if ret==True:

		t+=1	
		out.write(frame)

		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & t == 20:
		    break
	    else:
		break

	# Release everything if job is finished
	cap.release()
	out.release()
	cv2.destroyAllWindows()

	quality = raw_input('Good enough? 0/1 \n') 
if(emotion==7):
	emotion=1
	count+=1
else:	
	emotion+=1
# os.remove('count.py')
f=open('config.py','w')
f.write('count='+str(count)+';emotion='+str(emotion)+';')
f.close

print "\n"
if(emotion==1):
	print "Next emotion must be ANGER"
elif(emotion==2):
	print "Next emotion must be FEAR"
elif(emotion==3):
	print "Next emotion must be DISGUST"
elif(emotion==4):
	print "Next emotion must be CONTEMPT"
elif(emotion==5):
	print "Next emotion must be JOY"
elif(emotion==6):
	print "Next emotion must be SADNESS"
elif(emotion==7):
	print "Next emotion must be SURPRISE"

print "\n"
