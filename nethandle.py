
import requests
import time
import json
import hardware
from picrypto import AESCipher

class RequestManager():
	def __init__(self):
		self.SendNow = False
		self.controlInfoUrl = 'http://localhost/python/control.php'     #hardcoding is not recommended store in json //todo
		self.response = None 
		self.imageResponse = None
		self.imagePostUrl = 'http://localhost/python/uploder.php'
		self.authToken = None
		self.authUrl = 'http://someurl'
		self.encryptor = AESCipher('rishabh') #rishabh is the symmetric key // to be replaced with original secret key
		
	def authenticate(self):
		try:
			mac_Of_Pi = hardware.getMAC('eth0') 
			enc_mac = self.encryptor.encrypt(mac_Of_Pi)
			#comment following 2 lines in prod mode
			print 'encrypted mac'
			print enc_mac
			payload = {"CODE":"000","MSG":"SUCCESS","RESPONSE":{"DATA":enc_mac}} #encrypted mac to be sent 
			headers = {'content-type':'application/json'}
		# following to be uncommented when proper http functioninng is achieved 
		#	self.response = requests.post(self.authUrl, data=json.dumps(payload), headers=headers) #json response is returned
		#	try:
		#		res_json = json.loads(self.response)
		#		if(res_json['MSG'] == 'SUCCESS'):
		#			return res_json['RESPONSE']['token']    # returns the token to be used for further comm
		#	except (ValueError, KeyError, TypeError):
		#		print 'error in json'
		#		return 'error in json'
		
		# use following random json till then:
			try: 
				res_json = open('res.json','w').read
				res = json.loads(res_json)
				if(res['MSG'] == 'SUCCESS'):
					return res['RESPONSE']['token']
			except (ValueError,KeyError,TypeError):
				print 'error in json'
		except requests.ConnectionError:
			print 'Connection Error'
			
		
	def getApplianceControlInfo(self):
		try:
			payload = {"CODE":"000","MSG":"SUCCESS","RESPONSE":{"token":"SFSasfiojoij32432oi3jiojsa","command_name":[]}}
			headers =  {'content-type': 'application/json'}
			#self.response = requests.post(self.controlInfoUrl, data=json.dumps(payload), headers=headers)
			#return self.response.text
			json_res = open('controlInfo.json','w').read()
			res = json.loads(json_res)
			return res
		except requests.ConnectionError:
			time.sleep(1)
			print 'No Connection'
	
	def postImage(self,file):
		try: 
			self.imageResponse = requests.post(self.imagePostUrl,files=file)
			print self.imageResponse.text
		except requests.ConnectionError:
			time.sleep(2)
			print 'No Connection'
		
if __name__ == '__main__':
	print 'again in main'
	manger = RequestManager()
	#manger.getApplianceControlInfo()
	files = {'file': open('gpio.png', 'rb')}
	manger.postImage(files)
	
		