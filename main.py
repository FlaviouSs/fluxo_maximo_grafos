import graph

RedeFluxo = graph.Graph()

RedeFluxo.processar_entrada("entrada.txt")

print(RedeFluxo.arestas)

for _ in RedeFluxo.residual:
    print(_)