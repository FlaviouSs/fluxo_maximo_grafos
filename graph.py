class Graph:

    def __init__(self):
        self.numeroVertices = 0
        self.s = None
        self.t = None
        self.vertices = set()
        self.arestas = []
        
    def processar_entrada(self, path):

        with open(path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

            self.numeroVerices = int(lines[0])
            
            self.s = int(lines[1])
            self.t = int(lines[2])

            lines.pop(0), lines.pop(0), lines.pop(0)

            for line in lines:
                u, v, capacidade = line.split()
                
                u = int(u)
                v = int(v)
                capacidade = float(capacidade)

                self.vertices.add(v)
                self.vertices.add(u)
                self.arestas.append((u, v, capacidade))

            self.numeroVertices = len(self.vertices)

    