import os, json
lista_tarefas_excluidas = []

def commandTask(comando, listOfTask):
    isComand = verifyComand(comando)
    if isComand:
        execute(comando, listOfTask)
    else:
        add_task(comando, listOfTask)
    

def verifyComand(comando):
    if comando in ['listar', 'desfazer', 'refazer', 'cls', 'salvar tarefa', 'importar tarefas']:
        return True
    else:
        return False


def execute(comando, listOfTask):
    comandos = {
        'listar' : lambda: listar(listOfTask),
        'desfazer' : lambda: desfazer(listOfTask),
        'refazer' : lambda: refazer(listOfTask),
        'cls': lambda: clear(),
        'salvar tarefa': lambda: savetask(listOfTask),
        'importar tarefas': lambda: importarTarefas(listOfTask)
    }
    
    comandoo = comandos.get(comando)
    comandoo()

def add_task(tarefa, listOfTask):
    listOfTask.append(tarefa)    
    clear()


def listar(listOfTask):
    print()
    print('TAREFAS') 
    if verifyList(listOfTask):
        for num, tarefa in enumerate(listOfTask):
            print(f'{num + 1}. {tarefa}')
        print()
        
        
def desfazer(listOfTask):
    if verifyList(listOfTask):    
        transferTask(listOfTask, lista_tarefas_excluidas)
        listar(listOfTask)
    
    
def refazer(listOftTask):
    if verifyList(listOftTask):    
        transferTask(lista_tarefas_excluidas, listOftTask)
        listar(listOftTask)
    

def clear():
    os.system('cls')

    
def transferTask(listremove, listadd):
    taskTransfer = listremove.pop()
    listadd.append(taskTransfer)    


def verifyList(listVerify):
    if not listVerify: # Verifica se a lista está vazia ou não.
        print('Lista vazia...')
        return False 
    
    return True

# Salvando arquivo em JSON
def savetask(listTask):
    if verifyList(listTask):
        filesave = transformjson(listTask)
        with open('task.json', 'w', encoding='UTF-8') as arquivo:
            json.dump(filesave, arquivo, indent=2, ensure_ascii=False)
        
        print('Tarefa salva com sucesso!')
        return
    
    print('A tarefa não pode ser salva com a lista de tarefas vazia.')    

def transformjson(listTask):
    fileJSON = {}
    for numberTask, task in enumerate(listTask):
        fileJSON[numberTask] = task
    
    return fileJSON

# Importando as tarefas em JSON e transformando
def importarTarefas(listTasckRecive):
    try:
        with open('task.json', 'r', encoding='UTF-8') as arquivo:
            jsonTarefas = json.load(arquivo)
            if jsonTarefas == {}:
                print('O arquivo está vazio')
                return
            
        listTransfer = transformlist(jsonTarefas)
        for task in listTransfer:
            listTasckRecive.append(task)
            print(f'{task} adicionada com sucesso!')
        
        listTransfer.clear()
        esvaziarjson()
    except FileNotFoundError:
        print('O arquivo não foi e encontrado.')
            

def transformlist(jsonfiles):
    listTransfer = list()
    for task in jsonfiles.values():
        listTransfer.append(task)
    
    return listTransfer

def esvaziarjson():
    dados = dict()
    with open('task.json', 'w') as arquivo:
        json.dump(dados, arquivo)
        