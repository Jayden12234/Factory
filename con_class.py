
class Coneyer:
    def __init__(self, pos, dic):
        self.pos = pos
        self.dic = dic
        self.obj = None
    def add_conv(self, conv):
        if conv.pos==[self.pos[0]-self.dic[0], self.pos[1]-self.dic[1]]:
            self.conv = conv
    def send_obj(self):
        if self.obj != None:
            self.conv.obj = self.obj