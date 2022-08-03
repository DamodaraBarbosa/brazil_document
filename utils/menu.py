def linha():
    print('\033[1;33m--\033[m'*25)

def linha2():
    print('\033[1;33m-=\033[m'*25)

def show_menu():
    linha2()
    print('\tQUAL OPÇÃO DESEJA GERAR?')
    linha2()
    print('1. Cadastro de pessoa física (CPF).')
    print('2. Cadastro numérico de pessoa jurídica (CNPJ).')
    linha()
