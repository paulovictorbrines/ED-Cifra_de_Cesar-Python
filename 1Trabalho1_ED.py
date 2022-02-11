class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque

''' Primeira Tarefa - Decodificação da Lista de Missões '''
def adicionar_alfabeto(deque, alfabeto):
    for i in range(len(alfabeto)):
        deque.add_front(alfabeto[i])
    return None

def decifrar(deque, texto_cifrado, chave):
    alfabeto=str(deque)
    texto_cifrado=list(texto_cifrado)

    for i in range(len(texto_cifrado)):
        for x in alfabeto:
            if texto_cifrado[i]==x:
                texto_cifrado[i]=alfabeto.index(x)

    i=-1
    while i>(chave*-1)-1:
        deque.add_rear(alfabeto[i])
        deque.remove_front()
        i-=1
    
    alfabeto=str(deque)

    for i in range(len(texto_cifrado)):
        texto_cifrado[i]=alfabeto[texto_cifrado[i]]
    texto_plano=''.join(texto_cifrado)

    i=0
    while i<(chave):
        deque.add_front(alfabeto[i])
        deque.remove_rear()
        i+=1
    
    return texto_plano

''' Segunda Tarefa - Selecionar Subconjunto de Missões '''
def selecionar_subconjunto_missoes():

    W=int(input())
    M=int(input())
    O=int(input())
    A=str(input())
    C=int(input())
    N=int(input())

    lista_i=[]
    d=Deque() 
    adicionar_alfabeto(d,A)
    for _ in range(N):
        i=str(input())
        i=i[1:-1]
        i=decifrar(d, i, C)
        i,Wi,Vi,nivel=i.split(',')
        Wi,Vi=int(Wi),int(Vi)
        lista_i.append([i,Wi,Vi,nivel])

    n=len(lista_i)
    lista_Wi=[]
    for i in range(n):
        lista_Wi.append(lista_i[i][-3])
    lista_Vi=[]
    for i in range(n):
        lista_Vi.append(lista_i[i][-2])

    def mochila(W,lista_Wi,lista_Vi,n):
        matriz=[[0 for x in range(W+1)] for x in range(n+1)]

        for i in range(n+1):
            for j in range(W+1):
                if i==0 or j==0:
                    matriz[i][j]=0
                elif lista_Wi[i-1]>j:
                    matriz[i][j]=matriz[i-1][j]
                else:
                    matriz[i][j] = max(lista_Vi[i-1] + matriz[i-1][j-lista_Wi[i-1]], matriz[i-1][j])
            
        i=n
        j=W
        lista_Wi_total=[]
        lista_index=[]
        while matriz[i][j]>0:
            if matriz[i-1][j]!=matriz[i][j]:
                lista_Wi_total.append(lista_Wi[lista_Vi.index(lista_Vi[i-1])])
                lista_index.append(lista_Vi.index(lista_Vi[i-1])+1)
                j=j-lista_Wi[i-1]
            i-=1
        return lista_index,lista_Wi_total,matriz[n][W]

    mochila=mochila(W,lista_Wi,lista_Vi,n)

    lista_itotal=[]
    for i in range(len(mochila[0])):
        lista_itotal.append(lista_i[mochila[0][i]-1])

    if M==1:
        from operator import itemgetter
        if O==0:
            lista_itotal=sorted(lista_itotal,key=itemgetter(3))
            lista_itotal=sorted(lista_itotal,key=itemgetter(2))
            lista_itotal=sorted(lista_itotal,key=itemgetter(1))
            lista_itotal=sorted(lista_itotal,key=itemgetter(0))
        if O==1:
            lista_itotal=sorted(lista_itotal,key=itemgetter(3))
            lista_itotal=sorted(lista_itotal,key=itemgetter(2))
            lista_itotal=sorted(lista_itotal,key=itemgetter(0))
            lista_itotal=sorted(lista_itotal,key=itemgetter(1))
        if O==2:
            lista_itotal=sorted(lista_itotal,key=itemgetter(3))
            lista_itotal=sorted(lista_itotal,key=itemgetter(1))
            lista_itotal=sorted(lista_itotal,key=itemgetter(0))
            lista_itotal=sorted(lista_itotal,key=itemgetter(2))
        if O==3:     
            lista_itotal=sorted(lista_itotal,key=itemgetter(2))
            lista_itotal=sorted(lista_itotal,key=itemgetter(1))
            lista_itotal=sorted(lista_itotal,key=itemgetter(0))
            lista_itotal=sorted(lista_itotal,key=itemgetter(3))

        for x in lista_itotal:
            print(*x,sep=', ')
        print(f'Tempo restante: {W-sum(mochila[1])}')
        print(f'Valor: {mochila[2]}')

    else:
        print(f'Tempo restante: {W-sum(mochila[1])}')
        print(f'Valor: {mochila[2]}')
    
    return None



	
d = Deque()
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
adicionar_alfabeto(d, alfabeto)
texto_cifrado = 'XTYSLKNLCL'
print(f'texto_plano: {decifrar(d, texto_cifrado, len(alfabeto))}')
print(f'{str(d)}')
print(f'{len(str(d))}')