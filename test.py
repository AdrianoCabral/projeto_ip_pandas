 	
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

class carro:
    def __init__(self, marca, ano, kilometragem, cor,combustivel,motor, transmissão):  
        self.__marca = marca
        self.__ano = ano
        self.__kilometragem = kilometragem
        self.__cor = cor
        self.__combustivel = combustivel
        self.__motor = motor
        self.__transmissão = transmissão

    def getMarca(self):
        return self.__marca

    def getAno(self):
        return self.__ano
    
    def getKilometragem(self):
        return self.__kilometragem
    
    def getCor(self):
        return self.__cor

    def getCombustivel(self):
        return self.__combustivel
    
    def getMotor(self):
        return self.__motor
    
    def getTransmissão(self):
        return self.__transmissão


            
        


            

    #print(linha)

    arquivo.close()
    print('\n')


#dff.plot(kind='scatter',x='KM',y='Preco',color='blue')
#plt.show()