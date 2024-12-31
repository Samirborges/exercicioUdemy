import os
def menu(*args):
    while True:
        options = list(args)
        for num, option in enumerate(options):
            print(f'{num + 1}. {option}')
        
        choice = int(input('> '))
        verify = responseMenu(choice, options)
        if verify:
            return choice
        
            
def responseMenu(choiceUser, listOptions):
    if choiceUser > len(listOptions):
        os.system('cls')
        print('Oção inválida! Escolha uma opção válida.')
        return False
    
    return True


def insertInforClass():
    dadosPessoa = dict()
    dadosPessoa['nome'] = str(input('Digite o nome: '))
    dadosPessoa['idade'] = int(input('Digite a idade: '))
    dadosPessoa['emprego'] = str(input('Digite o emprego: '))
    dadosPessoa['salario'] = float(input('Digite o salário: R$'))
    
    return dadosPessoa