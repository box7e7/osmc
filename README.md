# osmc

pip3 install python-engineio==3.14.2 python-socketio[client]==4.6.0

https://pypi.org/project/python-socketio/


A complete Python client for the Kodi JSON-RPC API Resources:
https://github.com/haikuginger/kodipydent
pip3  install kodipydent

from kodipydent import Kodi
my_kodi = Kodi('localhost', username='kodi', password='s1ptest')
my_kodi.Player.Open(item={'file':'plugin://plugin.video.youtube/?action=play_video&videoid=DT4kQlM5xuE'})
