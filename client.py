
from utils.mask import Mask
from utils.menu import show_menu, linha

show_menu()

option = Mask(int(input('Digite a opção desejada: ')))

linha()

while True:
    option.document_validator()
    option.document_generator()
    if option.document_validator() == True:
        print(option.mask())
        break


