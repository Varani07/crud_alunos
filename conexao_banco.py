from mysql.connector import Error, connect

class ConexaoBanco:
    def get_connection(self):
        connection = None
        try:
            connection = connect(
                host="localhost",
                user="root",
                password="",
                database="crud_alunos")
        except Error as e:
            print(f"Erro ao conectar! {e}")
            connection.close()
        return connection