
class Resource:
    def __init__(self, map, pos, out_dic):
        self.map = map
        self.pos = pos
        self.out_dic = out_dic
        self.key = self.map.res_key
    def write(self):
        if self.map.map[self.pos[1]][self.pos[0]]!=0:
            self.map.write_val()