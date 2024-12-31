import json
from package.classPackage.Pessoa import Pessoa

def importclass():
    try:
        with open('dadosPessoa.json', 'r', encoding='UTF-8') as arquivo:
            inforClass = json.load(arquivo)
        
        pessoa = Pessoa(**inforClass)
        return pessoa
        
    except FileNotFoundError:
        print('Nenhuma classe foi salva. Não será possível importar uma classe.')