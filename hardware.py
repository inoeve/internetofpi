#py script to fetch mac address of pi
# author: rishabh
# created: dec-10-2014 @ 10:00pm
# script to fetch mac address of hardware

import json
#import RPi.GPIO as GPIO



#get mac address of pi
def getMAC(interface):
	try:
		  mac = open('/sys/class/net/%s/address' %interface).readline()
	except:
		  mac = "00:00:00:00:00:00"
	return mac
	

#switches functionality 	
class Switchable():
	def __init__(self,context,number):
		self.context = context
		self.number = number
		self.stateChart = None    # will help maintain state info dynamically throughout run time 
	def initialize(self):
	#	GPIO.setmode(GPIO.BOTH)           
		try: 
			mapjson = open('config/map.json','r').read()
			self.map = json.loads(mapjson)     #map is a dictionary
			keys = self.map.keys()
			for i in range(0,len(keys)):
			#	GPIO.setup( self.map[keys[i]],GPIO.OUT)
		except ValueError, KeyError:
			print 'error in json'
			
		
		
	def switchOn(self,number):
		print 'switched On %s',number
		print 'switched on %s',self.map[number]
		# GPIO.output(self.map[number],1)
		
	
	def switchOff(self,number):
		print 'switched off %s',number
		print 'switched off %s',self.map[number]
		# GPIO.output(self.map[number],0)
		
		
	def getState(self,number):
		return self.state
		# not operational yet
	
	def flipState(self,number):
		if self.state == True:
			self.state = False
		elif self.state == False:
			self.state = True
		# not operational yet
			
class Camera():
	def __init__(self,capture):
		self.context = context
		
	def capture(self):
		pass
		#code to capture image 
		#set to take 15 jpegs every second when turned on, and save them to resources/date/time.jpeg in compressed-encrypted format
		# date folder is to be created dynamically depending on the day 
		# a different service monitors the camera and removes jpegs in case: 1) they are sent to server, 2) they are older than X days 
	

	
