from socket import *
import sys
import message
from message import Message, ACK

from message_header import Header
from message_body import BodyData
from message_body import BodyRequest
from message_body import BodyResponse
from message_body import BodyResult
from message_util import MessageUtil


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 4000))

print('연결 확인 됐습니다.')
msgId = 0

reqMsg = Message()
test = ACK("asd",10,"0xasdasd","asd")
reqMsg.Body = BodyRequest(None)
reqMsg.Body.FILESIZE = 10
reqMsg.Body.FILENAME = "test"
reqMsg.Body.FILEIP = 15

msgId += 1
reqMsg.Header = Header(None)
reqMsg.Header.MSGID = msgId
reqMsg.Header.MSGTYPE = message.REQ_FILE_SEND
reqMsg.Header.BODYLEN = reqMsg.Body.GetSize()
reqMsg.Header.FRAGMENTED = message.NOT_FRAGMENTED
reqMsg.Header.LASTMSG = message.LASTMSG
reqMsg.Header.SEQ = 0

MessageUtil.send(sock, reqMsg)  # 클라이언트는 서버에 접속하자마자 파일 전송 요청 메세지를 보낸다.
rspMsg = MessageUtil.receive(sock)  # 그리고 서버의 응답을 받는다.

# clientSock.send('I am a client'.encode('utf-8'))

print('메시지를 전송했습니다.')

# data = clientSock.recv(1024)
# print('받은 데이터 : ', data.decode('utf-8'))
sock.close()