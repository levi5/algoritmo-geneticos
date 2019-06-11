
import random
from fitness import Fitness

class Cruzamento():                                   # Classe cruzamento 
    def __init__(self,TAM_Pop, populacao, NUM_CROM):  # Método construtor da classe 
        self.Tamanho_Populacao = TAM_Pop                # Variável tamanho da população
        self.populacao = populacao                      # População de indíviduos
        self.numCrom = NUM_CROM                         # Número de Cromossomos
        self.nova_Pop = []                              # Lista de nova população

    def geraCruzamento(self, Frase):                 # Método para gera os filhos 
        x1 = 4                                       # Ponto de corte 1
        x2 = 9                                       # Ponto de corte 2
        x3 = 14                                      # Ponto de corte 3
        cnt = 0
        listTmp = []
        while(len(listTmp) < self.Tamanho_Populacao):   # lopp. Enquanto o tamanho da lista filhos for menor que tamanho da população
            ind = self.populacao[cnt]                   # Variável 'ind' recebe o primeiro indivíduo
            p1 = ind[:x1]                               # corta o indivíduo em 3 pontos
            p2 = ind[x1:x2]
            p3 = ind[x2:x3]                             #

            cnt +=1 
            ind = self.populacao[cnt]                   # Variável 'ind' recebe o segundo indivíduo
            p4 = ind[0:x1]                              # corta o indivíduo em 3 pontos
            p5 = ind[x1:x2]                             
            p6 = ind[x2:x3]                             #

            t1 = p1 + p5 + p3                           # Produz um novo indivíduo(filho) com as partes cortadas
            t2 = p4 + p2 + p6                           # Produz um novo indivíduo(filho) com as partes cortadas
            t1.append(0)                                # Adiciona o valor 0 do fitness ao individuo 1
            t2.append(0)                                # Adiciona o valor 0 do fitness ao individuo 2
            
            F =  Fitness(Frase, self.numCrom)           # Calcula o fitness dos indivíduos
            listTmp.append(F.Calc_Fitness(t1))          # Adiciona o indivíduo na lista de filhos
            F =  Fitness(Frase, self.numCrom)           # Calcula o fitness dos indivíduos
            listTmp.append(F.Calc_Fitness(t2))          # Adiciona o indivíduo na lista de filhos
                                                        # repete o procedimento com mais dois individuos
        print("filhos")                                 # imprimi a lista de filhos
        for i in listTmp:
            print(i)
        return listTmp
           



            


