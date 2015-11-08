import threading
import time 



class InfoThread (threading.Thread):
	
	def __init__(self,delay,context):
		threading.Thread.__init__(self)
		self.delay = delay
		self.context = context
		self.isRunning = False
	
	def run(self):
		
		while(self.isRunning == True):
			print 'starting fetching info'
			#load json from httpmodule: 
			actionjson = self.context.getHandle('net').getApplicationControlInfo()
			self.context.getHandle('action').resolveAction(actionjson)
			#define what work u want to do use context to get functionality of other modules 
			print 'passing info json to action resolver'
			time.sleep(self.delay)
			
		
	def stop(self):
		self.isRunning = False

class DataThread (threading.Thread):
	
	def __init__(self,delay,context):
		threading.Thread.__init__(self)
		self.delay = delay
		self.context = context
		self.isRunning = False
	def run(self):
		isRunning = True
		while(self.isRunning):
				#define what work u want to do use context to get functionality of other modules 
				print 'starting data delivery'
				print 'getting images from resources'
				print 'passsing data to httphandle for post and waiting for green signal'
				print 'removing images from local resources'
				time.sleep(self.delay)
			
		
	def stop(self):
		self.isRunning = False
		