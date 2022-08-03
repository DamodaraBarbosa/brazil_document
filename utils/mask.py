from utils.generator import Generator

class Mask(Generator):
    def __init__(self, choice) -> None:
        super().__init__(choice)
    def mask(self):
        try:
            if len(self._document) == 11:
                return f'CPF gerado: {self._document[0:3]}.{self._document[3:6]}.{self._document[6:9]}-{self._document[9:]}'
            elif len(self._document) == 14:
                return f'CNPJ gerado: {self._document[:2]}.{self._document[2:5]}.{self._document[5:8]}/{self._document[8:12]}-{self._document[12:]}'
        except AttributeError:
            pass