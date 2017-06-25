import SocketServer

from handler import HCIRequestHandler
from tmdb3 import set_key
from tmdb3 import set_cache

Handler = HCIRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
set_key('43b0a2c458adc3c7d5968151b9599958')
set_cache('null')#TODO consider adding cache mechanism

server.serve_forever()