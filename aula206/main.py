from package.interface.interface import menu, insertInforClass
import os
from package.classPackage.Pessoa import Pessoa
from package.importClass import importclass

# Menu
while True:
    responce = menu('Criar pessoa', 'Salvar informações', 'Importar informações', 'Ver informações')

    match responce:
        case 1:
            os.system('cls')
            print('Criando nova pessoa...')
            print('Insira as informações')
            
            dadosPessoa = insertInforClass()
            
            pessoa = Pessoa(**dadosPessoa)
            os.system('cls')
            print('Pessoa criada com sucesso!')
            pessoa.imprimirinformacoes()
            input()
            
        case 2:
            print('Salvando informações...')
            pessoa.saveClass()
            
        case 3: 
            print('Importando informações...')
            pessoa = importclass()
            input('Importação da classe feito com sucesso!')
            
        case 4:
            try:
                pessoa.imprimirinformacoes()
                input()
            except:
                print('A classe não foi criada.')
                
    os.system('cls')