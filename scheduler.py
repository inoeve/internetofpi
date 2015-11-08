# class to schedule tasks at periodic intervals of time 
# usage: every class using this scheduler must define a performTask() which shall be executed on every tick
import time
class Scheduler():
	def __init__(self):
		self.KEEPUP = True
		self.count = 0
		
	def scheduleTask(self,job,period):
		while self.KEEPUP == True:
			time.sleep(period)
			job.performTask()    #every class looking to use this scheduler must define a performTask method
		quit()
	
	def toggleState(self):
		if self.KEEPUP == True:
			self.KEEPUP = False
		else:
			self.KEEPUP = True
		
	def startJobA(self,job): # job is a parent object which is using scheduler
		while self.KEEPUP == True:
			print "Sending http GET request to server"
			time.sleep(5)
			job.performTaskA()
		quit()
	
	def startJobB(self,jobB):
		while self.KEEPUP == True:
			print 'Sending http post request to server'
			time.sleep(7)
			jobB.performTAskB()
		quit()
	
	
	
# in case program to be used as main 
# only for testing purposes	
#if __name__ == '__main__':
#	print 'Got to main'
	
	