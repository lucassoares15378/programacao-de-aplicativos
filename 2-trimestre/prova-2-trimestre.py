import sqlite3

try:
    conexao = sqlite3.connect('armazem.db')
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print(f"Erro ao conectar o banco de dados: {erro}")
    exit()

def cadastrar_operadores():
    try:
        razao_social = input("Qual a razão social? ")
        inscricao_estadual = input("Qual a inscrição estadual? ")

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS operadores_logisticos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            razao_social TEXT NOT NULL,
            inscricao_estadual INTEGER
        )
        ''')

        comando_inserir = f'''
        INSERT INTO operadores_logisticos(razao_social, inscricao_estadual)
        VALUES('{razao_social}', '{inscricao_estadual}')
        '''

        cursor.execute(comando_inserir)
        conexao.commit()
        print("Cadastro feito com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados ao cadastrar: {erro}")


def listar_operadores():
    try:
        cursor.execute("SELECT * FROM operadores_logisticos")
        linhas = cursor.fetchall()
        if not linhas:
            print("Nenhum cadastro realizado!")
        else:
            for linha in linhas:
                print(f"ID: {linha[0]} | Razão Social: {linha[1]} | Inscrição Estadual: {linha[2]}")
        print("\n")

    except sqlite3.Error as erro:
        print(f"Erro ao listar operadores: {erro}")


def atualizar_operadores():
    try:
        id_operador = int(input("Qual o ID para realizar a atualização? "))

        cursor.execute(f'''SELECT * FROM operadores_logisticos WHERE id = {id_operador}''')
        operadores_logisticos = cursor.fetchone()

        if operadores_logisticos is None:
            print("ID não encontrado!")
        else:
            nova_razao_social = input("Digite a nova razão social: ")
            nova_inscricao_estadual = input("Digite a nova inscrição estadual: ")

            comando = f'''
            UPDATE operadores_logisticos 
            SET razao_social = '{nova_razao_social}',
            inscricao_estadual = '{nova_inscricao_estadual}'
            WHERE id = {id_operador}
            '''

            cursor.execute(comando)
            conexao.commit()
            print("Dados atualizados com sucesso!")

    except ValueError:
        print("Valor inválido")

    except TypeError:
        print("Tipo de dado inválido")

    except ZeroDivisionError:
        print("Divisão por zero")

    except FileNotFoundError:
        print("Arquivo não encontrado")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")

def excluir_operadores():
    try:
        id_operador = int(input("Qual o ID para realizar a exclusão? "))

        cursor.execute(f"SELECT * FROM operadores_logisticos WHERE id = {id_operador}")
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
        print(f"Erro ao excluir registro: {erro}")


def cadastrar_galpão():
    try:
        identificacao_bloco = input("Qual a identificação do bloco? ")
        id_operador = int(input("Qual o ID do operador? "))

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS galpoes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            comando_inserir = f'''
            INSERT INTO galpoes(identificacao_bloco, id_operador)
            VALUES('{identificacao_bloco}', '{id_operador}')
            '''
            cursor.execute(comando_inserir)
            conexao.commit()
            print("Galpão cadastrado!")

    except ValueError:
        print("O ID precisa ser um número inteiro!")
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados ao cadastrar: {erro}")

def listar_galpoes():
    try:
        cursor.execute("SELECT * FROM galpoes")
        linhas = cursor.fetchall()
        if not linhas:
            print("Nenhum cadastro realizado!")
        else:
            for linha in linhas:
                print(f"ID: {linha[0]} | Identificação do bloco: {linha[1]} | ID Operador: {linha[2]}")
        print("\n")

    except sqlite3.Error as erro:
        print(f"Erro ao listar galpões: {erro}")


def atualizar_galpoes():
    try:
        id_galpao = int(input("Qual o ID para realizar a atualização? "))

        cursor.execute(f'''SELECT * FROM galpoes WHERE id = {id_galpao}''')
        galpao = cursor.fetchone()

        if galpao is None:
            print("ID não encontrado!")
        else:
            nova_identificacao_bloco = input("Digite a nova identificação do bloco: ")
            novo_id_operador = int(input("Digite o novo ID operador: "))

            cursor.execute(
                f"SELECT * FROM operadores_logisticos WHERE id = {novo_id_operador}"
            )
            operador = cursor.fetchone()

            if operador is None:
                print("Nenhum operador com esse ID cadastrado!")
            else:
                comando = f'''
                UPDATE galpoes 
                SET identificacao_bloco = '{nova_identificacao_bloco}',
                id_operador = {novo_id_operador}
                WHERE id = {id_galpao}
                '''

                cursor.execute(comando)
                conexao.commit()
                print("Dados atualizados com sucesso!")

    except ValueError:
        print("Valor inválido")

    except TypeError:
        print("Tipo de dado inválido")

    except ZeroDivisionError:
        print("Divisão por zero")

    except FileNotFoundError:
        print("Arquivo não encontrado")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")

def excluir_galpoes():
    try:
        id_galpao = int(input("Qual o ID para realizar a exclusão? "))

        cursor.execute(f"SELECT * FROM galpoes WHERE id = {id_galpao}")
        galpao_existe = cursor.fetchone()

        if galpao_existe is None:
            print("Nenhum galpão encontrado")
        else:
            cursor.execute(f"DELETE FROM galpoes WHERE id = {id_galpao}")
            conexao.commit()
            print("Galpão excluído com sucesso!")

    except ValueError:
        print("O ID precisa ser um número inteiro!")
    except sqlite3.Error as erro:
        print(f"Erro ao excluir registro: {erro}")


def menu():
    while True:
        try:
            print("\n1. Cadastrar Operador")
            print("2. Listar Operadores")
            print("3. Alterar Operador")
            print("4. Excluir Operador")
            print("5. Cadastrar Galpão")
            print("6. Listar Galpões")
            print("7. Alterar Galpão")
            print("8. Excluir Galpão")
            print("9. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cadastrar_operadores()
            elif opcao == '2':
                listar_operadores()
            elif opcao == '3':
                atualizar_operadores()
            elif opcao == '4':
                excluir_operadores()
            elif opcao == '5':
                cadastrar_galpão()
            elif opcao == '6':
                listar_galpoes()
            elif opcao == '7':
                atualizar_galpoes()
            elif opcao == '8':
                excluir_galpoes()
            elif opcao == '9':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

        except KeyboardInterrupt:
            print("\n\nExecução interrompida. Fechando o sistema de forma segura...")
            break
        except Exception as erro:
            print(f"Ocorreu um erro inesperado no menu: {erro}")
    try:
        conexao.close()
    except:
        pass


menu()