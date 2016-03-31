#!/usr/bin/env python
# riesal@gmail.com
# simple python socket client with
# - socket lingering disabled (send RST flag)
# - socket REUSEADDR enabled
# - socket nonblocking
#
# Usage: pync.py yourserverip yourport
import time,sys,socket
from struct import pack

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, pack('ii', 1, 0))
s.connect(( sys.argv[1], int(sys.argv[2]) ))
while 1:
    data = sys.stdin.read(100)
    if not data: break
    s.send(data)
    s.settimeout(0.0)
    s.shutdown(socket.SHUT_WR)
    s.close()

