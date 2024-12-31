def menuOptions(listOption, autenticar=False):
    while True:
        for numberOption, options in enumerate(listOption):
            numberOption += 1
            print(f'\033[1;36m{numberOption}.\033[m \033[1;33m{options}\033[m')
            
        if autenticar:
            numberOptions = len(listOption)
            choiceUser = int(input('> '))
            
            if choiceUser > numberOptions:
                    print('\033[1;31mERRO!\033[31m Opção inválida. Tente novamente.\033[m')
                    
            else:
                    return choiceUser
                
