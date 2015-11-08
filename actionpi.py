import time

class ActionPi():
	light = None
	camera = None
	
	def __init__(self):
		self.light = False
		self.camera = False
	
	def switchOn(self,id):
		print id
		if id == None:
			print ' no connection'
		else:
			print 'camera'
	
	def switchOff(self,id):
		print id
		print 'switched off'

class ActionResolver():
	def __init__(self,context):
		self.context = context
		self.jsonNetInfo = None
		self.map = json.loads(open('config/map.json','r').read())
		self.v_pin = json.loads(open('config/v_pin.json','r').read())
		
		
	def resolveAction(self,jsonInfo):
		self.jsonNetInfo = jsonInfo
		
	
		
		
	