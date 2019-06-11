
import random
from individuo import Individuo
from  fitness import Fitness

class Mutacao():                                # Classe Mutação

    def __init__(self, TAMPop,numCrom, listaFilho,listaSelec, Taxa_Mutac, caracter):
        self.lista_Filho = listaFilho
        self.lista_Selec = listaSelec
        self.TAM_Pop     = TAMPop
        self.NUM_CROM    = numCrom
        self.TX_Mutac    = Taxa_Mutac
        self.Caract      = caracter

    def gera_Mutacao(self, Frase):                 # Método para gerar mutação no filhos
        listaTmp = []
        listaFin = []
        listaFinal = []
        TX_Mut_A = round(random.random())          # Número aleatorio entre 0 e 1
        for x in self.lista_Filho:
            
            if(TX_Mut_A  <= self.TX_Mutac):       # Se o número aleatorio for menor e igual que taxa de mutação, o indivíduo sofre a mutação em 2 duas posições aleatorias
                x1 = random.randint(0, self.NUM_CROM-1)  # x1 = valor de posição aleatoria
                x2 = random.randint(0, self.NUM_CROM-1)  # x2 = valor de posição aleatoria
                I = Individuo(self.Caract)               # instancia clase indivíduo
                x[x1] = I.get_caracter()                 # Modifica o caracter na posição x1 por um novo caracter na mesma posição
                x[x2] = I.get_caracter()                 # Modifica o caracter na posição x2 por um novo caracter na mesma posição
                F =  Fitness(Frase, self.NUM_CROM)       # Recalcula o Fitness
                listaTmp.append(F.Calc_Fitness(x))
            else:                                        # Caso a condição não seja aceita
                listaTmp.append(x)                       # Adicione o indivíduo na lista sem alteração

        print('Mutação nos Filhos')                      # imprimi os filhos com ou sem mutação
        for y in listaTmp:
            print(y)

        for z in self.lista_Selec:                      # Adiciona os filhos e pais dentro de uma lista
            listaFin.append(z)
        for z in listaTmp:
            listaFin.append(z)

        listaFin.sort(key=lambda x: x[self.NUM_CROM]) # Ordena a lista de pais e filhos
        for x in range(self.TAM_Pop, len(listaFin)):  # gera uma lista com o melhor dos pais e filhos
            listaFinal.append(listaFin[x])

        print('Nova População')                       # imprimi a lista com os melhores
        for y in listaFinal:
            print(y)

        return listaFinal                             # retorna a lista com nova população

