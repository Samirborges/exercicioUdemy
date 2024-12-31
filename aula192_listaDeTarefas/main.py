# Vai criar uma lista e colocar um input para o usuário digitar qualquer coisa. Onde vai digitar tarefas ou qualquer comando.
'''
Essos comandos vão ser:
    1. Listar: Mostrar uma lista de tarefas
    2. Desfazer
    3. Refazer
essas duas ultimas é como se fosse o ctrl+z e ctrl+shift+z
'''
from package.listTask import commandTask

tasks = []
while True:
    print('LISTA DE TAREFAS')
    print('Comandos: listar, desfazer, refazer, salvar tarefa, importar tarefas')
    
    comand = str(input('Digite um comando ou uma tarefa: '))
    commandTask(comand, tasks)
    