

from individuo import Individuo             # Importa a classe Indivíduo
from fitness import Fitness                 # Importa a classe Fitness 

class Populacao():                          # Classe População
    def __init__(self, TAM_Pop, frase):     # Método construtor da classe 
        self.listPop    = []
        self.Frase      = frase

    def Gera_PopInic(self, caracter, TAM_Pop, NUM_CROM):    # Gera uma população inicial
    
        for x in range(0 , TAM_Pop):                # Laço para 
            IND = Individuo(caracter)               # Variável recebe indivíduo
            F = Fitness(self.Frase, NUM_CROM)       # A Variável F recebe instancia da classe fitness
            self.listPop.append(F.Calc_Fitness(IND.Gera_Individuo(NUM_CROM))) # Adiciona o individuo na lista de populações e calcula o Fitness 
            print(self.listPop[x])                  # imprimi o indivíduo
        return self.listPop                         # retorna a lista de indivíduos

