
import random

class Map:
    def __init__(self, conv_key, har_key, slm_key, mat_key, out_f):
        self.size = [15,15]
        self.out_f = out_f
        self.res_key = mat_key
        self.map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        self.conv_key = conv_key
        self.har_key = har_key
        self.slm_key = slm_key
        self.res = 'metal'
    def map_gen(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if random.randint(0,10)==2:
                    self.map[j][i] = self.res_key
    def write_val(self,pos,val):
        self.map[pos[1]][pos[0]] = val
    def output(self):
        with open(self.out_f, 'w') as file:
            for i in range(self.size[1]):
                file.write(str(self.map[i]))