import socket
import time
from config import config
import json

def register(content):
    url = config.get_config('register')
    if url == 'none': return
    auth = config.get_config('authorization')
    if auth == 'none': return

    header = 'Content-Type: application/json\r\nAuthorization: Basic %s\r\n' % auth
    jsondata = json.dumps(content)
    http_post(url, header, jsondata)

def http_post(url, header, content):
    _, _, host, path = url.split('/', 3)
    if ':' in host:
        host, port = host.split(':')
        port = int(port)
    else:
        port = 80
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.settimeout(5) # otherwise it will wait forever
    try:
        s.connect(addr)
    except:
        return
    l = len(content)
    xmsg = bytes('POST /%s HTTP/1.1\r\nHost: esp8266\r\nContent-Length:%d\r\n%s\r\n' % (path, l, header), 'utf8')
    try:
        s.send(xmsg)
        s.sendall(content)
        s.close()
    except:
        return
    print('Registered')

