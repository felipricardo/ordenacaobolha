lista = [10,20,30,40,50]
#OMITIR O ALGORITMO DA BOLHA
#LISTA DEVE ESTAR ORDENADA
print("Dgite o numero procurado: ")
procurado = int(input())
ini = 3
#fim = 4 #ultima casa da lista
fim = len(lista) - 1
while ini <= fim:
    meio = int((ini + fim) / 2)
    if procurado == lista[meio]:
        print("Achei")
        break
    if procurado > lista[meio]:
        ini = meio + 1
    if procurado < lista[meio]:
        fim = meio - 1
if not ini <= fim:
    print("Não encontrado...")
