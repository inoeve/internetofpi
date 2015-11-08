import json

config = open('res.json','r').read()
try: 
	res = json.loads(config)
	print res['bye']
except (ValueError,KeyError,TypeError):
				print 'error in json'
