
arquivo = 'regist.txt'


    
def escolha():
    
    while True:
    
        print('''\nEscolha uma da opções abaixo:\n
    1- Adicionar cadastro
    2- Apagar Cadastro
    3- Conferir todos os cadastros
    4- Encerrar o programa''')
    
        opcao = int(input('\nDigite sua opção:'))
             
    
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
    
    

def adicionar():
    
    while True:
        
        sair = str(input('\nPara voltar ao menu digite [s] ou pressione enter para continuar:')).upper()
        
        if sair == 'S':
            break
        
        nome = str(input('\nDigite o nome:'))
        cpf = int(input('Digite o número do cpf:'))
        idade = int(input('Digite a idade:'))
        sexo = str(input('Digite o sexo:'))
        print('''Qual o seu gênero:
        1- Cis
        2- Trans
        3- Não-Binário
        4- Prefiro não dizer''')
        genero = int(input('Qual a sua opção:'))
        email = str(input('Digite seu e-mail:'))
        tel = int(input('Digite o número do telefone:'))
    
        if genero == 1:
            genero = 'Cis'
        
        elif genero == 2:
            genero = 'Trans'
                
        elif genero == 3:
            genero = 'Não-Binário'
        
        elif genero == 4:
            genero = 'Prefiro não dizer'
        
        
        salvar =str(input('\nSalvar o cadastro[S/N]:')).upper()
    
        if salvar =='S':
            
            
            arq = open(arquivo,'at') 
            arq.write(f'\nNome:{nome}\nCPF:{cpf}\nIdade:{idade}\nSexo:{sexo}\nGênero:{genero}\nE-mail:{email}\nTelefone:{tel}\n')
            arq.close()
             
            print('\nCadastro adicionado com sucesso!')
            
            
        adicionar = str(input('\nGostaria de adicionar mais algum cadastro[S/N]:')).upper()
            
        if adicionar == "N":
            break


def apagar():
    
    while True:
        try:
            excluir = int(input('\nDigite o número do cpf do cliente que você gostaria de remover([0] para voltar ao menu):'))
            
            if excluir == 0:
                break 
            
            certeza = str(input('\nTem certeza que gostaria de excluir esse cadastro[S/N]:')).upper()
            
            if certeza == 'S':
                cadastros = []
                with open('regist.txt', 'r') as arquivo:
                    dados_cadastros = arquivo.read().split('\n\n')  
                    for dados in dados_cadastros:
                        cadastro = dados.strip().split('\n')  
                        cadastros.append(cadastro)

                found = False
                novos_cadastros = []
                for cadastro in cadastros:
                    if len(cadastro) >= 2:
                        cpf = int(cadastro[1].split(':')[-1])  
                        if excluir != cpf:
                            novos_cadastros.append(cadastro)
                        else:
                            found = True

                if found:
                    with open('regist.txt', 'w') as arquivo:
                        for cadastro in novos_cadastros:
                            arquivo.write('\n'.join(cadastro) + '\n\n')  
                    print('\nCadastro removido com sucesso!')
                else:
                    print('\nCPF não encontrado')

            else:
                break

        except ValueError:
            print('\nCPF inválido. Digite um número inteiro.')
               
            
                 
def ver():
    
    arq = open('regist.txt','rt')
    print(arq.read())
    
    while True:
        cont = str(input('Voltar ao menu[S]:')).upper()
        
        if cont == 'S':
            break
    
    
    
    
    
    