import graph

RedeFluxo = graph.Graph()

RedeFluxo.processar_entrada("entrada.txt")

print(RedeFluxo.arestas)

for _ in RedeFluxo.residual:
    print(_)

#x = RedeFluxo.fordFulkerson(RedeFluxo.s, RedeFluxo.t)
#print(x)

x = RedeFluxo.edmonds_karp(RedeFluxo.s, RedeFluxo.t)
print(x)

