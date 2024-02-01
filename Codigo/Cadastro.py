from opcoes import *

while True:
    
    print('-'*34)
    print('\033[1;36mFormulário de Cadastro de Pessoas\033[m')
    print('-'*34)


    print(''' Escolha uma das opções abaixo:\n
    1- Adicionar cadastro
    2- Apagar Cadastro
    3- Conferir todos os cadastros
    4- Encerrar o programa\n ''')

    opcao = int(input('Digite sua opção:'))

    if opcao == 1:           
            adicionar()
            
            if arquivo == '':
                arq = open(arquivo,'wt+')
                arq.close()
            else:
                arq = open(arquivo,'at')      
                    
    if opcao == 2:
        apagar()
        
    elif opcao == 3:
        ver()

    elif opcao == 4:
        break





print('\n\033[1;36mPrograma finalizado!\033[m')






