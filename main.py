# -*- coding: utf-8 -*-

from  populacao import  Populacao                       # Importa a classe População
from    selecao import    Selecao                       # Importa a classe Seleção
from cruzamento import Cruzamento                       # Importa a classe Cruzamento
from    mutacao import    Mutacao                       # Importa a classe Mutação 

def is_frase(populacao, NUM_CROM):                      # Método para verificar se o melhor Fitness foi encontrado 
        for x in populacao:                             # Percorre toda população em busca dos Fitness 
                if (x[NUM_CROM] == NUM_CROM):           # Compara o valor do Fitness 
                        return False                    # retorna False se valor do melhor Fitness for encontrado 
        return True                                     # retorna True  se valor do melhor Fitness não for encontrado 

def main():                                                             # Método principal(main)
    caracter = '!, .:;?áÁãÃâÂõÕôÔóÓéêÉÊíQWERTYUIOPASDFGHJKLÇZXCVBNMqwertyuiopasdfghjklçzxcvbnm1234567890'  # Caracteres aceitáveis 
    frase = list("Im an iron man")                              # Frase deverá ser encontrada
    Tamanho_Populacao     = 100                                 # Tamanho da População
    NUM_CROM    = len(frase)                                    # Número  de Cromossomos
    Taxa_Selec  =  0.6                                          # Taxa de seleção
    Taxa_Mutac  =  0.6                                          # Taxa de mutação
    populacao   = [ ]                                           # variáveis Temporárias
    listaSelec  = [ ]
    listaFilh   = [ ]
    listaN_POP  = [ ]
   
 
    #Cria a População Inicial
    print("População Inicial")
    print("_"*40)
    P = Populacao (Tamanho_Populacao, frase)                            # variável P recebe uma instancia da classe população
    populacao = P.Gera_PopInic(caracter, Tamanho_Populacao, NUM_CROM)   # método para geração da população inicial

    num_geracao = 0
    while(is_frase(populacao, NUM_CROM)):                               #
            # Seleção 
            S = Selecao(Taxa_Selec, populacao, NUM_CROM, Tamanho_Populacao)     # Variável S recebe uma instancia da classe Seleção 
            listaSelec =  S.selecao_Torneio(3)                                  # O Método Seleção por Torneio retorna uma lista de indivíduos selecionados
            #listaSelec =  S.selecao_roleta()

            # Cruzamento
            C = Cruzamento(Tamanho_Populacao,listaSelec, NUM_CROM)              # Variável C recebe a classe Cruzamento  
            listaFilh =  C.geraCruzamento(frase)                                # O Método Cruzamento com varios pontos de corte retorna uma lista de filhos
            
            # Mutação
            M = Mutacao(Tamanho_Populacao, NUM_CROM, listaFilh, populacao, Taxa_Mutac,caracter) # Variável M recebe a uma instancia da classe Mutação  
            listaN_POP = M.gera_Mutacao(frase)                                  # O Método de Mutação por caracter aleatório retorna uma lista de indivíduos que sofreram ou não mutação
            
            populacao = listaN_POP                      # Variável população recebe nova população
            Tamanho_Populacao = len(populacao)          # Variável tamanho da população recebe o novo tamanho da população
            num_geracao += 1                            # Variável 'num_geracao' e incrementada

            print("ciclo {}".format(num_geracao))       # Imprimi o número de ciclos


main()


