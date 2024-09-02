from conexao_banco import ConexaoBanco
from mysql.connector import Error

class DeleteDAO:
    def __init__(self):
        self.connection = ConexaoBanco().get_connection()
        self.cursor = self.connection.cursor()

    def deletar(self, tabela: str, where: str, valor_dados: tuple, tipo: str):
        try:
            sql = f"DELETE FROM {tabela} WHERE {where}"
            sc0 = "SET FOREIGN_KEY_CHECKS=0"
            sc1 = "SET FOREIGN_KEY_CHECKS=1"

            self.cursor.execute(sc0)
            self.cursor.execute(sql, valor_dados)
            self.cursor.execute(sc1)

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