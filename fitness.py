
class Fitness():                            # Classe Fitness
    def __init__(self, frase, NUM_CROM ):   # Construtora
        self.Frase = frase                  # Frase a ser encontrada
        self.numCrom = NUM_CROM             # Número de cromossomos

    def Calc_Fitness(self, list_Ind):       # Método para calcular o fitness
        cont = 0
        for x in range(0, self.numCrom):    # pecorre todo indivíduo comparando os seu caracteres e sua posições com os da frase
            c1 = self.Frase[x]
            c2 = list_Ind[x]
            if(c1 == c2):                   # se ouve uma correspondência 
                cont += 1                   # incrementa a variável cont
        list_Ind[self.numCrom] = cont       # Adiciona o valor final do fitness a ultima posição do indivíduo
        return list_Ind                     # retorna o indivíduo 
