from conexao_banco import ConexaoBanco
from mysql.connector import Error

class DAO():
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
        
    def visualizar(self, dados: str, tabela: str, where: str, valor_dados: tuple, one: bool):
        try:
            sql = f"SELECT {dados} FROM {tabela}{where}"

            if valor_dados == "":
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql, valor_dados)
            
            if one:
                result = self.cursor.fetchone()
            else:
                result = self.cursor.fetchall()


            self.cursor.close()
            return result
        
        except Error as e:
            print()
            print(f"*ERRO! {e.msg}")
            print()
            print("- - - - - - - - - - - - - - - - - - - - - - ")
            print()
        finally:
            if self.connection.is_connected:
                self.connection.close()

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