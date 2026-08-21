import sqlite3

try:
    conexao = sqlite3.connect('armazem.db')
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print(f"Erro ao conectar o banco de dados: {erro}")
    exit()

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
            return nova_razao_social, nova_inscricao_estadual
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
       
assert atualizar_operadores() == ("shopee", "2323")