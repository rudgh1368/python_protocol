from message_body import RREQ
from message_header import Header
from message import Message

import sys
from test3 import RREQ2

reqMessage = Message()

body = RREQ("0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0",
               "0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0",
               "0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0",
               100,
               ["0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0", "0x35bB94eB7DDce99DEbf7e482Fb9f30203Ba32DC0"],
               [100,200])

bodyLen =sys.getsizeof(body)
print("bodyLen :", bodyLen)
header = Header(5, 3, bodyLen)

reqMessage.Body = body
reqMessage.Header = header

byte = reqMessage.GetBytes()
print(sys.getsizeof(byte))


