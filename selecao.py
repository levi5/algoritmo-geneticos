
import random
import heapq 
class Selecao():                                                            # Classe Seleção
    def __init__(self,Taxa_selecao, populacao,num_Cromossomo, Tamanho_Pop): # Método construtor
        self.Taxa_Selecao  = Taxa_selecao                                   # Taxa de seleção
        self.Cromossomos   = num_Cromossomo                                 # Número de Cromossomos
        self.Populacao     = populacao                                      # População
        self.Tamanho_Pop   = Tamanho_Pop                                    # Tamanho da População
        self.lista_Selecao = []
    
    def soma_fitness(self):
        soma = 0
        for fitness in self.Populacao:
            soma = soma + int(fitness[self.Cromossomos])
        return soma

    
    def selecao_roleta(self):                                       #Método seleção por roleta
        
        self.Populacao.sort(key=lambda x: x[self.Cromossomos])
        while(len(self.lista_Selecao) != self.Tamanho_Pop):
            self.Populacao.sort(key=lambda x: x[self.Cromossomos])
            soma = self.soma_fitness()
            #r = round (random.uniform(0, soma), 2)
            r = random.randint(0, soma)
            i = 0
            aux = self.Populacao[i][self.Cromossomos]
            while(aux < r):
                i = i + 1
                aux = aux + int(self.Populacao[i][self.Cromossomos])

            self.lista_Selecao.append(self.Populacao[i])
        
        print("Selecão por Roleta")
        for i in self.lista_Selecao:
            print(i)
        return self.lista_Selecao

#########################################
    def ind(self, N):
        lista_individuos = []
        for x in range(0 , N):
            n = random.randint(0, self.Tamanho_Pop-1)
            while(True):
                if (n in lista_individuos):
                    n = random.randint(0, self.Tamanho_Pop-1)
                else:
                    lista_individuos.append(n)
                    break
        return lista_individuos

    def selecao_Torneio(self, N):                                   # Método Seleção por Torneio

        while(len(self.lista_Selecao ) != self.Tamanho_Pop):        #loop.Enquanto o tamanho da lista seleção for diferente do tamanho da população
            sx = self.ind(N)                                        # A variável 'sx' recebe lista com números dos indivíduos sorteados
            lista_Individuos = []                                   
            for individuo in sx:                                    
                lista_Individuos.append(self.Populacao[individuo])  # Adiciona na lista os indivídos selecionados aleatoriamente 

            r = random.random()                                     # valor aleatorio entre 0 e 1 
            neext = 0
            after = 0
            tmp   = 0
            after =  lista_Individuos[0]                           # A variável 'after' recebe o primeiro indivíduo da lista
            if(r < self.Taxa_Selecao):                             # se r for menor que taxa de seleção
                for x in range(0, len(sx)):                        # os indivíduos são comparados ate encontrar entre os N o que possui o melhor fitness
                    neext = lista_Individuos[x]
                    if(neext[self.Cromossomos] >= after[self.Cromossomos]):
                        tmp = neext
                    elif(neext[self.Cromossomos] < after[self.Cromossomos]):
                        tmp = after
                    after = neext
                self.lista_Selecao.append(tmp)                      # adiciona o indivíduo selecionado a lista, e execulta o loop ate a condição não for mais aceita
        print()
        print("Selecão por Torneio")                                # imprimi a lista de indivíduos selecionados 
        for x in self.lista_Selecao:
            print(x)   
        return self.lista_Selecao                                   # retorna lista de indivíduos selecionados



    

                   


