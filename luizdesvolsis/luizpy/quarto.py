class Quarto:
    def __init__(self, num, type, value, boolean):
        self.__num = num
        self.__type = type
        self.__value = value
        self.__boolean = boolean

    def exibir_detalhes(self):
        print(f'Número da casa: {self.__num}')
        print(f'Tipo da casa: {self.__type}')
        print(f'Valor de reserva: {self.__value}')
        if self.__boolean == True:
            print(f'Disponibilidade: DISPONIVEL')
        else:
            print(f'Disponibilidade: INDISPONIVEL')    
        print()
        
    def reservar(self):
        if self.__boolean == True:
            self.__boolean = False 
            print(f'Casa reservada')
        else:
            print(f'Quarto não disponivel')

    def liberar(self):
        if self.__boolean == False:
            self.__boolean = True
            print(f'Quarto liberado')
        else:
            print(f'Quarto já disponivel ')

    def alterar_preco(self, value):
        if value <= 0:
            print(f'Valor inválido')
        else:
            self.__value = value     