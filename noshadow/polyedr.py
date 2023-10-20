from math import pi
from common.r3 import R3
from common.tk_drawer import TkDrawer


class Edge:
    """ Ребро полиэдра """    

    def __init__(self, beg, fin):
        self.beg, self.fin = beg, fin


class Facet:
    """ Грань полиэдра """
 
    def __init__(self, vertexes):
        self.vertexes = vertexes


class Polyedr:
    """ Полиэдр """
   
    def __init__(self, file):
        
        self.vertexes, self.edges, self.facets = [], [], []
      
        with open(file) as f:
            for i, line in enumerate(f):
                if i == 0:                   
                    buf = line.split()                    
                    c = float(buf.pop(0))  
                    alpha, beta, gamma = (float(x) * pi / 180.0 for x in buf)
                elif i == 1:
                    nv, nf, ne = (int(x) for x in line.split())
                elif i < nv + 2:
                    x, y, z = (float(x) for x in line.split())
                    self.vertexes.append(R3(x, y, z).rz(
                        alpha).ry(beta).rz(gamma) * c)
                else:
                    buf = line.split()
                    size = int(buf.pop(0))
                    vertexes = [self.vertexes[int(n) - 1] for n in buf]
                    for n in range(size):
                        self.edges.append(Edge(vertexes[n - 1], vertexes[n]))
                    self.facets.append(Facet(vertexes))

    def draw(self, tk):
        tk.clean()
        for e in self.edges:
            tk.draw_line(e.beg, e.fin)
