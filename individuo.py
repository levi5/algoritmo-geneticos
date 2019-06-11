
from random import randint                  # 

class Individuo():                          # Classe Indivíduo 
    def __init__(self, caracter):           # Método de inicialização da classe indivíduo 
        self.listaC     = []                # Lista de lista de caracteres 
        self.listInd    = []                # lista de indivíduos 
        self.set_caracter(caracter)         # Chamada do método para converter String em uma lista de caracteres

    def set_caracter(self, caracter):       # Método para converter String em uma lista de caracteres
        for x in caracter:
            self.listaC.append(x)           #

    def Gera_Individuo(self, NUM_CROM):     # Método para geração de indivíduos
        tam = len(self.listaC)              # Tamanho da lista de caracter
  
        for x in range(0 , NUM_CROM+1):                 # Laço para geração de indivíduos com genes aleatórios 
            y = randint(0, tam-1)                       # Gera um valor y aleatório entre 0 e tamanho da lista de caracter
            if(x < NUM_CROM):
                self.listInd.append(self.listaC[y])     # Adiciona o caracter no individuo
            elif (x >= NUM_CROM):                       
                self.listInd.append(0)                  # adiciona o valor 0 (valor de fitness inicial) no indivíduo
        return self.listInd                             # Retorna uma lista com os genes do indivíduo

    def get_caracter(self):                 # Método retorna um caracter aleatório
        tam = len(self.listaC)
        num = randint(0, tam-1)
        x = self.listaC[num]
        return x



  