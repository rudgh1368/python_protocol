from message import ISerializable
import message
import struct


class RREQ(ISerializable):  # 파일 전송 요청 메세지(0x01)에 사용할 본문 클래스이다. FILESIZE와 FILENAME 데이터 속성을 갖는다.
    def __init__(self, buffer):
        if buffer != None :
            fmt = "=32s32s32sii"

            unpacked = struct.unpack(fmt, buffer[0:104])
            print('unpack', len(unpacked))
            self.initiator = unpacked[0].decode(encoding='utf-8').replace('\x00', '')
            self.target = unpacked[1].decode(encoding='utf-8').replace('\x00', '')
            self.sender = unpacked[2].decode(encoding='utf-8').replace('\x00', '')
            self.amount = unpacked[3]
            self.path_len = unpacked[4]

            path_fmt = str(self.path_len * 32) + "s"
            path_balance_fmt = str(self.path_len) + "i"
            unpacked = struct.unpack(path_fmt, buffer[104:104 + self.path_len * 32])
            print("test unpacked : {}".format(len(unpacked)))
            path = (unpacked[0].decode(encoding='utf-8').replace('\x00', ''))
            chunks, chunk_size = len(path), int(len(path)/self.path_len)
            self.path = [path[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
            print("path", self.path)
            unpacked = struct.unpack(path_balance_fmt, buffer[104 + self.path_len * 32:])
            print("test unpacked : {}".format(len(unpacked)))
            self.path_balance = []
            for i in unpacked: self.path_balance.append(i)

            self.struct_fmt = str.format(fmt + path_fmt + path_balance_fmt, len(buffer))
            self.struct_len = struct.calcsize(self.struct_fmt)
            print("test {},{},{},{}, {}".format(fmt, path_fmt, path_balance_fmt, self.struct_fmt, self.struct_len))

        else :
            self.struct_fmt = 0
            self.struct_len = 0
            self.initiator = ""
            self.target = ""
            self.sender = ""
            self.amount = 0
            self.path_len = 0
            self.path = ""
            self.path_balance = ""

    def set(self, initiator, target, sender, amount, path, path_balance):
        fmt = "=32s32s32sii"
        path_fmt = str(len(path) * 32) + "s"
        path_balance_fmt = str(len(path_balance)) + "i"
        self.struct_fmt = str.format(fmt + path_fmt + path_balance_fmt, 0)
        self.struct_len = struct.calcsize(self.struct_fmt)
        self.initiator = initiator
        self.target = target
        self.sender = sender
        self.amount = amount
        self.path_len = len(path)
        self.path = ""
        self.path_balance = path_balance

        for i in path : self.path += i
        # for i in path_balance: self.path_balance += bytes(i)

    def unpack(self, buffer):
        fmt = "=32s32s32sii"

        unpacked = struct.unpack(fmt, buffer[0:104])
        print('unpack', len(unpacked))
        self.initiator = unpacked[0].decode(encoding='utf-8').replace('\x00', '')
        self.target = unpacked[1].decode(encoding='utf-8').replace('\x00', '')
        self.sender = unpacked[2].decode(encoding='utf-8').replace('\x00', '')
        self.amount = unpacked[3]
        self.path_len = unpacked[4]

        path_fmt = str(self.path_len * 32) + "s"
        path_balance_fmt = str(self.path_len) + "i"
        unpacked = struct.unpack(path_fmt, buffer[104:104 + self.path_len * 32])
        print("test unpacked : {}".format(len(unpacked)))
        self.path = []
        for i in unpacked : self.path.append(i.decode(encoding='utf-8').replace('\x00', ''))

        unpacked = struct.unpack(path_balance_fmt, buffer[104 + self.path_len * 32:])
        print("test unpacked : {}".format(len(unpacked)))
        self.path_balance = []
        for i in unpacked: self.path_balance.append(i)

        self.struct_fmt = str.format(fmt + path_fmt + path_balance_fmt, len(buffer))
        self.struct_len = struct.calcsize(self.struct_fmt)
        print("test {},{},{},{}, {}".format(fmt, path_fmt, path_balance_fmt, self.struct_fmt, self.struct_len))

    def GetBytes(self):
        # buffer = self.FILENAME.encode(encoding='utf-8')
        # 1 unsigned long long, N character
        # self.struct_fmt = str.format('=Q{0}s', len(buffer))

        return struct.pack(
            self.struct_fmt,
            *(
                self.initiator.encode(),
                self.target.encode(),
                self.sender.encode(),
                self.amount,
                self.path_len,
                self.path.encode(),
                *self.path_balance
            ))

    def GetSize(self):
        # buffer = self.FILENAME.encode(encoding='utf-8')
        #
        # # 1 unsigned long long, N character
        # self.struct_fmt = str.format('=Q{0}s', len(buffer))
        # self.struct_len = struct.calcsize(self.struct_fmt)
        return self.struct_len
