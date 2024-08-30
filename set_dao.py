from conexao_banco import ConexaoBanco
from mysql.connector import Error

class setDAO:
    def __init__(self):
        self.connection = ConexaoBanco().get_connection()
        self.cursor = self.connection.cursor()

    def cadastrar_curso(self, curso: tuple):
        try:
            sql = "INSERT INTO cursos (nome_curso, sigla) VALUES (%s, %s)"
            self.cursor.execute(sql, curso)
            self.connection.commit()
            self.cursor.close()
            print("---------------------------------")
            print("| CURSO CADASTRADO COM SUCESSO! |")
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