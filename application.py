# binds together all classes from different modules to attain complete functionality of app
from scheduler import *
from nethandle import *
from actionpi import *
from jobthread import *
import threading
import time

class Application():
	app_scheduler = None
	app_httpHandle = None
	controlInfo = None
	app_actionpi = None
	app_infoThread = None
	
	def __init__(self):
		self.app_scheduler = Scheduler()
		self.app_httpHandle = RequestManager()
		self.controlInfo = None
		self.app_actionpi = ActionPi()
		self.app_actionResolver = ActionResolver()
		self.security_token = None
		self.app_infoThread = infoThread(5,self)
		self.app_dataThread = dataThread(10,self)
		self.live = True
		self.testCount = 0
	
	def startLoop(self):
		# step1: authentication
		# step2: ask for control info     #every 5 seconds
		# step3: send data //log files or images    # based on some flag or availability or scheduling 
		# step4: use multi threading for control flow and data flow 
		#self.app_scheduler.startJobA(self)
		# start 2 threads and pass functions 2 be performed to them authentication => fetch control info
		self.security_token = self.app_httpHandle.authenticate(); # one time authentication, #step 1
		print self.security_token;
		self.app_infoThread.start()
		self.app_dataThread.start()
		while (self.testCount < 4):
				self.testCount = self.testCount + 1
				time.sleep(2)
		
		self.app_infoThread.stop()
		self.app_dataThread.stop()
		
	def performTaskA(self):
		self.controlInfo = self.app_httpHandle.getApplianceControlInfo()
		print self.controlInfo
		self.app_actionpi.switchOn('camera')
	
	def performTaskB(self):
		pass
		
	def getHandle(code):
		if(code == 'net'):
			return self.app_httpHandle
		elif(code == 'action'):
			return self.app_actionResolver
	
	
		
if __name__ == '__main__':
	app = Application()
	app.startLoop()       
	