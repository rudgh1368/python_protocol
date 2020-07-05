from message import ISerializable
import struct

class Header(ISerializable):
    def __init__(self, buffer):
        if buffer != None :
            self.struct_fmt = '=3I'  # 3 unsigned int, 2 byte, 1 unsigned short
            self.struct_len = struct.calcsize(self.struct_fmt)

            unpacked = struct.unpack(self.struct_fmt, buffer)
            self.MSGID = unpacked[0]
            self.MSGTYPE = unpacked[1]
            self.BODYLEN = unpacked[2]
        else :
            self.struct_fmt = '=3I' # 3 unsigned int, 2 byte, 1 unsigned short
            self.struct_len = struct.calcsize(self.struct_fmt)

    def set(self, msgID, msgTYPE, bodyLEN):
        self.MSGID = msgID
        self.MSGTYPE = msgTYPE
        self.BODYLEN = bodyLEN

    def unpack(self, buffer):
        self.struct_fmt = '=3I'  # 3 unsigned int, 2 byte, 1 unsigned short
        self.struct_len = struct.calcsize(self.struct_fmt)

        unpacked = struct.unpack(self.struct_fmt, buffer)
        self.MSGID = unpacked[0]
        self.MSGTYPE = unpacked[1]
        self.BODYLEN = unpacked[2]

    def GetBytes(self):
        return struct.pack(
            self.struct_fmt,
            *(
                self.MSGID,
                self.MSGTYPE,
                self.BODYLEN,
            ))

    def GetSize(self):
        return self.struct_len