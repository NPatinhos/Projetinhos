from criando_usuario import cadastrar_usuario, listar_usuarios, apagar_usuario

def menu():
    print('______________________________')
    print('O QUE VOCÊ DESEJA FAZER?')
    print('1) Fazer cadastro')
    print('2) Deletar usuário')
    print('3) Ver usuários')  
    print('4) Sair')  
    print('______________________________')

while True:
    menu()
    opcao = input('Digite uma opção: ').strip()

    match opcao:
        case '1':
            cadastrar_usuario()
        case '2':
            apagar_usuario()        
        case '3':
            listar_usuarios()
        case '4':
            print('Encerrando programa...')
            break
        case _:
            print('Digite uma opção válida')
