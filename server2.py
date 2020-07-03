from socket import *
import sys
import message
from message import Message

from message_header import Header
from message_body import BodyData
from message_body import BodyRequest
from message_body import BodyResponse
from message_body import BodyResult
from message_util import MessageUtil

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 4000))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

reqMsg = MessageUtil.receive(connectionSock)
print(reqMsg)
# data = connectionSock.recv(1024)
# print('받은 데이터 : ', data.decode('utf-8'))

# connectionSock.send('I am a server.'.encode('utf-8'))
# print('메시지를 보냈습니다.')

serverSock.close()