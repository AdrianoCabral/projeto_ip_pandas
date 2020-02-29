 	
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import re

class Carro:
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

    def __str__(self):
        pass

lista_carros = []
for i in range(1,16):
    arquivo = open('test' + str(i) + '.txt', 'r')
    marca = ''
    ano = 0
    kilometragem = 0
    cor = ''
    combustivel = ''
    motor = 0.0
    transmissão = ''
    flano = False
    fkm = False
    fCor = False
    fComb = False
    fMotor = False
    fTrans = False
    fMarca = False
    fMarca2 = False
    for linha in arquivo:
        
        #print(linha)
        if  i > 200:
            print("yohoho")
        else:

            if(fMarca2 == True):
                marca = linha
                fMarca2 = False    
            elif(re.findall('\AMarca', linha)):
                fMarca2 = True

            elif(flano == True):
                linha = linha.replace(' ', '')
                lista = linha.split('/')
                ano = int(lista[1])
                flano = False
            elif(re.findall('\AANO', linha) or re.findall('\AAno', linha)):
                flano = True

            elif(fkm == True):
                kilometragem = int(linha)
                fkm = False    
            elif(re.findall('\AKM', linha) or re.findall('\AQuilometragem', linha)):
                fkm = True
                    
            elif(fCor == True):
                cor = linha
                fCor = False    
            elif(re.findall('\ACOR', linha) or re.findall('\ACor', linha)):
                fCor = True
            
            elif(fComb == True):
                combustivel = linha
                fComb = False    
            elif(re.findall('\ACombustível', linha)):
                fComb = True

            elif(fMotor == True):
                motor = float(linha)
                fMotor = False    
            elif(re.findall('\APotência do motor', linha)):
                fMotor = True            

            elif(fTrans == True):
                transmissão = linha
                fTrans = False    
            elif(re.findall('\ACâmbio', linha)):
                fTrans = True
            else:
                    for word in linha.split():
                        #print(word)
                        if(fMarca == False):
                            marca = word
                            #print('olha a marca aqui: {}'.format(marca))
                            fMarca = True
                            
                        else:
                            
                            if(fComb == True):
                                combustivel = word
                                fComb = False
                            if(word == 'Combustível:'):
                                fComb = True
                            
                            if(fMotor == True):
                                motor = float(word)
                                fMotor = False
                            if(word == 'Motor:'):
                                fMotor = True
                            
                            if(fTrans == True):
                                transmissão = word
                                fTrans = False
                            if(word == 'Transmissão:'):
                                fTrans = True
    #print(marca, ano, kilometragem, cor)
    c1 = Carro(marca, ano, kilometragem, cor, combustivel, motor, transmissão)
    #print(c1.getMarca(), c1.getAno(), c1.getKilometragem(), c1.getCor(), c1.getCombustivel(), c1.getMotor(), c1.getTransmissão())
    lista_carros.append(Carro(marca, ano, kilometragem, cor, combustivel, motor, transmissão))
    #print(lista_carros[0])

 
    #print(linha)

    arquivo.close()
    #print(lista_carros[0].getMarca())
    #print('\n')

for c1 in lista_carros:
    #print(c1.getMarca(), c1.getAno(), c1.getKilometragem(), c1.getCor(), c1.getCombustivel(), c1.getMotor(), c1.getTransmissão())
    print(c1.getMarca())
    print(c1.getAno())
    print(c1.getKilometragem())
    print(c1.getCor())
    print(c1.getCombustivel())
    print(c1.getMotor())
    print(c1.getTransmissão())

    print('\n')
#dff.plot(kind='scatter',x='KM',y='Preco',color='blue')
#plt.show()