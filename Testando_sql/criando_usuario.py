from database import conectar, desconectar

def cadastrar_usuario():
    nome = input('Qual seu nome?\n')
    usuario = input('Qual seu usuario?\n')
    senha = input('Digite sua senha: \n')


    conexao, cursor = conectar()

    try:
        cursor.execute("INSERT INTO usuarios (nome, usuario, senha) VALUES (?, ?, ?)", (nome, usuario, senha))
        conexao.commit()
        print("✅ Usuário cadastrado com sucesso!")
    except Exception as e:
            print(f"❌ Erro ao cadastrar usuário: {e}")
    finally:
            desconectar(conexao)

def listar_usuarios():
    conexao, cursor = conectar()

    cursor.execute("SELECT id, nome, usuario FROM usuarios")
    usuarios = cursor.fetchall()
    
    if usuarios: #é true
        print('Usuários:\n')
        for usuario in usuarios:
             print(f'Nome: {usuario[1]} - Nome de usuário: {usuario[2]}')
    else:
          print('Nenhum usuário cadastrado')
    desconectar(conexao)

def apagar_usuario():
    listar_usuarios()

    id_usuario = input('Digite o ID do usuário que será deletado: ')

    # Verificação se o ID é um número
    if not id_usuario.isdigit():
        print("❌ ID inválido. Digite um número.")
        return

    # 🔍 Correção: Converter para inteiro
    id_usuario = int(id_usuario)

    conexao, cursor = conectar()

    try:
        # Executa o comando SQL para deletar o usuário
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))

        # Verifica se algum registro foi afetado
        if cursor.rowcount > 0:
            conexao.commit()
            print("✅ Usuário deletado com sucesso!")
        else:
            print("❌ ID não encontrado. Verifique e tente novamente.")

    except Exception as e:
        print(f"❌ Erro ao tentar deletar usuário: {e}")
    
    # Fecha a conexão
    desconectar(conexao)
