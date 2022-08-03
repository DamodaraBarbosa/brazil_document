from utils.validator import Validator
from random import randint


class Generator(Validator):
    def __init__(self, choice) -> None:
        super().__init__(choice)
    
    def document_generator(self):
        if self.choice == 1:
            cpf = ''
            
            for digit in range(1, 12):
                cpf += f'{randint(0, 9)}'
            self._document = cpf

        elif self.choice == 2:
            cnpj = ''
                    
            for digit in range(1, 9):
                cnpj += f'{randint(0, 9)}'
            
            cnpj += '0001'
            
            for digit in range(1, 3):
                cnpj += f'{randint(0, 9)}'
            self._document = cnpj