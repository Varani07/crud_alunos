from conexao_banco import ConexaoBanco
from mysql.connector import Error

class SetDAO:
    def __init__(self):
        self.connection = ConexaoBanco().get_connection()
        self.cursor = self.connection.cursor()

    def cadastrar(self, tabela: str, dados: str, values: str, valor_dados: tuple, tipo: str):
        try:
            sql = f"INSERT INTO {tabela} ({dados}) VALUES ({values})"

            self.cursor.execute(sql, valor_dados)

            self.connection.commit()
            self.cursor.close()

            print(f"| {tipo.upper()} COM SUCESSO! |")
            print("---------------------------------------------------------")
            print()

        except Error as e:
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected:
                self.connection.close()