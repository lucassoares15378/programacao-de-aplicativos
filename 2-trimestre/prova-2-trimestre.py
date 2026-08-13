import sqlite3
try:
    conexao = sqlite3.connect('armazem.db')
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print(f"Erro ao conectar o banco de dados {erro}")
    exit()

def cadastrar_operadores():
    try:
        razao_social = input("Qual a razão social? ")
        inscricao_estadual = input("Qual a inscrição estadual? ")
    
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS operadores_logisticos (
                id INTEGER PRIMARY AUTOINCREMENT,
                razao_social TEXT NOT NULL,
                inscricao_estadual INTEGER
            )
            ''')
        comando_inserir = f'''
        INSERT INTO operadores_logisticos(razao_social, inscricao_estadual)
        VALUES('{razao_social}', '{inscricao_estadual}')'''

        cursor.execute(comando_inserir)
        conexao.commit()
        print("Cadastro feito com sucesso!")

    except sqlite3.Error as erro:
        print(f"Não foi possível conectar o banco de dados: {erro}.")

def listar_operadores():
    try:
        cursor.execute('SELECT FROM * operadores_logisticos')
        linhas = cursor.fetchall()
        if not linhas:
            print("Nenhum cadastro realizado!")
        else:
            for linha in linhas:
                print(f'''ID {linha[0]} | Razão Social {linha[1]} | Inscrição Estadual {linha[2]}''')
            print("\n")
    except sqlite3.Error as erro:
        print(f"Erro ao conectar banco de dados: {erro}.")

def atualizar_operadores():
    try:
        id_operador = int(input("Qual o ID para realizar a atualização? "))
        cursor.execute(f"SELECT FROM * operadores_logisticos WHERE id = {id_operador}")
        operadores_logisticos = cursor.fetchall()

        if operadores_logisticos is None:
            print("ID não encontrado!")
        else:
            nova_razao_social = input("Digite a nova razão social: ")
            nova_inscricao_estadual = input("Digite a nova inscrição estadual: ")
        
            comando = f''' UPDATE operadores_logisticos SET = razao social = '{nova_razao_social}',inscricao estadual = '{nova_inscricao_estadual}' WHERE id = {id_operador}'''
            cursor.execute(comando)
            conexao.commit()
            print("Dados atualizados")
    except sqlite3.Error as erro:
        print(f"Erro ao conectar banco de dados {erro}")
    except ValueError:
        print("Valor inválido!")
    except TypeError:
        print("Tipo de dao inválido!")
    except FileNotFoundError as erro:
        print(f"Ocorreu um erro: {erro}")
        
def excluir_operadores():
    try:
        id_operador = int(input("Qual o ID para realizar a exclusão? "))
        cursor.execute(f"SELECT FROM * operadores_logisticos WHERE id = {id_operador}")
        operador_existe = cursor.fetchone()

        if operador_existe is None:
            print("Nenhum operador encontrado")
        else:
            cursor.execute(f"DELETE FROM operadores_logisticos WHERE id = {id_operador}")
            conexao.commit()
            print("Operador excluído com sucesso!")
    except ValueError:
        print("O ID precisa ser um número inteiro!")
    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar banco de dados!")

def cadastrar_galpão():
    try:
        identificacao_bloco = input("Qual a identificação do bloco? ")
        id_operador = input("Qual o ID do operador? ")
    
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS galpoes (
                id INTEGER PRIMARY AUTOINCREMENT,
                identificacao_bloco TEXT NOT NULL,
                id_operador INTEGER,
                FOREIGN KEY(id_operador) REFERENCES operadores_logisticos(id)       
            )
            ''')
        cursor.execute(f"SELECT * FROM operadores_logisticos WHERE id = {id_operador}")
        operador = cursor.fetchone()

        if operador is None:
            print("Nenhum operador com esse ID cadastrado!")
        else:
            comando_inserir = f''' INSERT INTO galpoes (identificacao_bloco, id_operador)
            VALUES ('{identificacao_bloco}', '{id_operador}')
            '''
            cursor.execute(comando_inserir)
            conexao.commit()
            print("Galpão cadastrado!")
    except sqlite3 as erro:
        print("Erro ao conectar o banco de dados!")
    except ValueError:
        print("O ID precisa ser um número inteiro!")

def listar_galpoes():
    try:
        cursor.execute(''''SELECT FROM * galpoes''')
        linhas = cursor.fetchall()
        if not linhas:
            print("Nenhum cadastro realizado!")
        else:
            for linha in linhas:
                print(f'''ID {linha[0]} | Identificação de bloco {linha[1]} | ID Operador {linha[2]}''')
            print("\n")
    except sqlite3.Error as erro:
        print(f"Erro ao conectar banco de dados: {erro}.")

def atualizar_galpoes():
    try:
        id_galpao = int(input("Qual o ID para realizar a atualização? "))
        cursor.execute(f"SELECT FROM * operadores_logisticos WHERE id = {id_galpao}")
        galpao = cursor.fetchall()

        if galpao is None:
            print("ID não encontrado!")
        else:
            nova_identificacao_bloco = input("Digite a nova identificação do bloco: ")
            novo_id_operador = input("Digite o novo ID operador: ")
        
            comando = f''' UPDATE galpoes SET = identificacao bloco = '{nova_identificacao_bloco}', WHERE id = {id_operador}'''
            cursor.execute(comando)
            conexao.commit()
            print("Dados atualizados")
    except sqlite3.Error as erro:
        print(f"Erro ao conectar banco de dados {erro}")
    except ValueError:
        print("Valor inválido!")
    except TypeError:
        print("Tipo de dao inválido!")
    except FileNotFoundError as erro:
        print(f"Ocorreu um erro: {erro}")
        
def excluir_galpoes():
    try:
        id_operador = int(input("Qual o ID para realizar a exclusão? "))
        cursor.execute(f"SELECT FROM * operadores_logisticos WHERE id = {id_operador}")
        operador_existe = cursor.fetchone()

        if operador_existe is None:
            print("Nenhum operador encontrado")
        else:
            cursor.execute(f"DELETE FROM operadores_logisticos WHERE id = {id_operador}")
            conexao.commit()
            print("Operador excluído com sucesso!")
    except ValueError:
        print("O ID precisa ser um número inteiro!")
    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar banco de dados!")




def menu():
    while True:
        try:
            print("===SISTEMA DE CADASTRO LOGÍSTICO===")
            print("1- CADASTRAR OPERADOR")
            print("2- LISTAR TUDO CADASTADO")
            print("3- ATUALIZAR CADASTRO")
            print("4- DELETAR CADASTRO")

            opcao = int(input("Escolha uma opção: "))
            if opcao == '1':
                cadastrar_operadores()
            elif opcao == '2':
                listar_operadores()
            elif opcao == '3':
                atualizar_operadores()
            elif opcao == '4':
                excluir_operadoes()

        except KeyboardInterrupt:
            print("\n\nExecução interrompida. Fechando o sistema de forma segura...")
            break
        except Exception as erro:
            print(f"Ocorreu um erro inesperado no menu: {erro}")
    try:
        conexao.close()
    except:
        pass

def menu():