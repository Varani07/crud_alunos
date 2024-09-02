from conexao_banco import ConexaoBanco
from mysql.connector import Error

class UpdateDAO:
    def __init__(self):
        self.connection = ConexaoBanco().get_connection()
        self.cursor = self.connection.cursor()

    def atualizar(self, tabela: str, dados: str, where: str, tipo: str, valor_dados: tuple):
        try:
            sql = f"UPDATE {tabela} SET {dados} WHERE {where}"

            self.cursor.execute(sql, valor_dados)

            self.connection.commit()
            self.cursor.close()

            print(f"| {tipo.upper()} COM SUCESSO! |")
            print("---------------------------------")
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