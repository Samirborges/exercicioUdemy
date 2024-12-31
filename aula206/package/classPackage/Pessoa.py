import json
from time import sleep

class Pessoa:
    def __init__(self, nome, idade, emprego, salario):
        self.nome = nome
        self.idade = idade
        self.emprego = emprego
        self.salario = salario
        
    def imprimirinformacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'emprego: {self.emprego}')
        print(f'Salário: R${self.salario :.2f}')
        
    def saveClass(self):
        dadosJson = vars(self)
        with open('dadosPessoa.json', 'w', encoding='UTF-8') as arquivo:
            json.dump(dadosJson, arquivo, indent=2, ensure_ascii=False)

        print('Arquivo salvo com sucesso!')
        sleep(2.5)
        
    