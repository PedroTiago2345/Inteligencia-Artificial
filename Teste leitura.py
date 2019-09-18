file = open("C:/Users/17233313.LAB-INF/Downloads/Dados.txt","r")
CIDADES = file.readlines() #recebe o texto do .txt
file.close()
file = open("C:/Users/17233313.LAB-INF/Downloads/Dados2.txt","r")
CidadeinicioFim = file.readlines() # recebe cidade de imcio e fim
file.close()


SemEspaço = [] #usado para tirar os espaços
SemEspaço2 = [] #usado para tirar espaços
SemVirgula = [] #usado para tirar as virgulas
SemVirgula2 = [] #usado para tirar as virgulas
ListaCidades = []


###removendo espaços da lista###

def RemoveEspaço(lista):

    local = lista
    retorno = []
    for i in local:
       i = ''.join(i.split())
       retorno.append(i)
       
    return retorno

###separar em lista as cidades conectadas e remover virgula###

def ArrumaListaConexão(lista):
    local = lista
    retorno = []
    
    for i in local:
        i = i.split(",")
        a = i[0]
        b = i[1]
        b = b.replace(";","")
        retorno.append(a)
        retorno.append(b)

    return retorno
###separar e remover virgula na lista inicio fim###

def ArrumaInicioFim(lista):
    local = lista
    retorno = []
    
    for i in local:
        b = i
        b = b.replace(";","")
        retorno.append(b)

    return retorno

###removendo copias de cidade###

def ListarCidades(lista):
    local = lista
    retorno = []
    for i in local:
        if i not in ListaCidades:
            retorno.append(i)
    return retorno

            
###Criador do dicionario usado###
def Grafo(data):
    D = {}
    for n  in range(0, len(data)):
        key = data[n]
        if n+1 < len(data):
            value = data[n+1]
        if key not in D:
            D[key] = [value]
        else:
            D[key].append(value)
    return D
    


def largura(grafo, começo, destino):
    #uma fila que se inicia com a cidade de origem
    fila = []
    fila.append([começo])
    #enquanto a fila não estiver vazia, fará tal processo
    while fila:
        #pega o primeiro caminho (rota) da fila
        caminho = fila.pop(0)
        #pega o último nó do caminho
        node = caminho[-1]
        #caso o caminho tenha sido encontrado
        if node == destino:
            return caminho
        #vizinhos recebe o grafo a partir do nó atual
        vizinhos = grafo[node]
        #se um vizinho estvier no grafo de vizinhos
        #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
        #a fila adiciona a rota
        for vizinho in vizinhos:
            rota = list(caminho)
            rota.append(vizinho)
            fila.append(rota)

#busca em profundidade (Depth-First Search) entre cidade de origem e cidade de destino
def profundidade(grafo, começo, fim):
    #uma pilha que se inicia com a cidade de origem
    pilha = []
    pilha.append([começo])
    #enquanto a pilha não estiver vazia, fará tal processo
    while pilha:
        #pega o primeiro caminho da pilha
        caminho = pilha.pop()
        #pega o último nó do caminho
        node = caminho[-1]
        #caso o caminho tenha sido encontrado
        if node == fim:
            return caminho
        #neighbours (vizinhos) recebe o grafo a partir do nó atual
        elif node in grafo:
            vizinhos = grafo[node]
        #se um vizinho estiver no grafo de vizinhos
        #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
        #a pilha adiciona a rota
            for vizinho in vizinhos: 
                rota = list(caminho)
                rota.append(vizinho)
                pilha.append(rota)





SemEspaço = RemoveEspaço(CIDADES)
SemEspaço2 = RemoveEspaço(CidadeinicioFim)
SemVirgula = ArrumaListaConexão(SemEspaço)
SemVirgula2 = ArrumaInicioFim(SemEspaço2)
ListadeCidades = ListarCidades(SemVirgula)

origem = SemVirgula2[0]
destino = SemVirgula2[1]

grafo = Grafo(SemVirgula)

print("Rota gerado(largura) ->", largura(grafo,origem,destino))
print("Rota gerado(profundidade) ->", profundidade(grafo,origem,destino))


