import subprocess
import re
import json
import socketio


sio = socketio.Client()
sio.connect('https://redhat.goown.space:3000')
print('my sid is', sio.sid)

@sio.on('youtubeAPI')
def print_message(data):
	print(f' ############## ${data} #############')
	process = subprocess.Popen(['bash', '/home/osmc/youtubeAPI.sh', f"{data}"], stdout=subprocess.PIPE,stderr = subprocess.PIPE) 
	stdout,stderr= process.communicate()
	#sio.disconnect()
	print(stdout)

