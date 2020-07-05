from socket import *
import sys
import message
from message import Message

from message_header import Header
from message_body import RREQ
from message_util import MessageUtil


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 4000))

print('연결 확인 됐습니다.')
msgId = 0

reqMessage = Message()

body = RREQ(None)
body.set("0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0",
               "0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0",
               "0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0",
               100,
               ["0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0", "0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0"],
               [100,200])

bodyLen =sys.getsizeof(body)
print("bodyLen :", bodyLen)
header = Header(None)
header.set(5, 3, body.struct_len)

reqMessage.Body = body
reqMessage.Header = header

MessageUtil.send(sock, reqMessage)  # 클라이언트는 서버에 접속하자마자 파일 전송 요청 메세지를 보낸다.
# rspMsg = MessageUtil.receive(sock)  # 그리고 서버의 응답을 받는다.

# clientSock.send('I am a client'.encode('utf-8'))

print('메시지를 전송했습니다.')

# data = clientSock.recv(1024)
# print('받은 데이터 : ', data.decode('utf-8'))
sock.close()