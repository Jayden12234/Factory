
class Resource:
    def __init__(self, map, pos, out_dic):
        self.map = map
        self.pos = pos
        self.out_dic = out_dic
        self.key = self.map.res_key
        self.item = False
    def write(self):
        if self.map.map[self.pos[1]][self.pos[0]]!=0:
            self.map.write_val(self.pos,self.key)
    def add_conv(self, conv):
        if conv.pos == [self.pos[0]-self.out_dic[0], self.pos[1]-self.out_dic[1]]:
            self.item = True
            self.conv = conv
    def send_obj(self):
        if self.item==True:
            self.conv.obj = self.map.res
    