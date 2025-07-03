class Graph:

    def __init__(self):
        self.numeroVertices = 0
        self.s = None
        self.t = None
        self.vertices = set()
        self.arestas = []
        self.residual = None
        
    def processar_entrada(self, path):

        with open(path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

            self.numeroVertices = int(lines[0])
            
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

        matriz = [[0 for _ in range(self.numeroVertices)] for _ in range(self.numeroVertices)]
        
        for aresta in self.arestas:
            matriz[aresta[0]][aresta[1]] = aresta[2]
        
        self.residual = matriz

    def __dfs(self, s, t, visitado=None, caminho=None):
        
        if visitado is None:
            visitado = [False] * self.numeroVertices
        if caminho is None:
            caminho = []

        visitado[s] = True
        caminho.append(s)

        if s == t:
            return caminho
        
        for index, valor in enumerate(self.residual[s]):
            if not visitado[index] and valor > 0:
                caminho_aumentante = self.__dfs(index, t, visitado, caminho.copy())
                if caminho_aumentante:
                    return caminho_aumentante
                
        return None
    
    def fordFulkerson(self, fonte, sumidouro):
        fluxo_maximo = 0

        caminho = self.__dfs(fonte, sumidouro)
        while caminho:
            caminho_fluxo = float("Inf")
            
            for i in range(len(caminho) - 1):
                u, v = caminho[i], caminho[i + 1]
                caminho_fluxo = min(caminho_fluxo, self.residual[u][v])

            for i in range(len(caminho) - 1):
                u, v = caminho[i], caminho[i + 1]
                self.residual[u][v] -= caminho_fluxo
                self.residual[v][u] += caminho_fluxo

            fluxo_maximo += caminho_fluxo

            caminho = self.__dfs(fonte, sumidouro)

        return fluxo_maximo