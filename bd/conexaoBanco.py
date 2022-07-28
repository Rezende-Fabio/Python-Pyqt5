import pyodbc

class Conexao:  
    def crinado_conexao():
        dados_conexao = (
            "DRIVER={SQL Server};"
            "SERVER=1235412;"
            "DATABASE=Teste;"
            "UID=teste;"
            "PWD=1234;"
        )
        conexao = pyodbc.connect(dados_conexao)
        return conexao    


class Querys:
    def insert_usuario_login(con, usuario, senha):
        cursor = con.cursor()
        comando = f"""INSERT INTO usuario(nome, usuario, senha1, senha2, senha3, ativo)
        VALUES ('{usuario}', '{senha}', 1) """
        cursor.execute(comando)

    def inserir_usuario(con, nome, usuario, senha):
        try:
            cursor = con.cursor()
            comando = f"""INSERT INTO usuario(nome, usuario, senha1, senha2, senha3, ativo)
            VALUES ('{nome}', '{usuario}', '', '', '{senha}', 1) """
            cursor.execute(comando)
            cursor.commit()
        except:
            return False
        else: return True
    
    def verica_login(con, usuario, senha):
        cursor = con.cursor()
        comando = f"""SELECT ul.usuario, ul.senha FROM usuario_login ul"""
        usuarios = cursor.execute(comando)
        for x in usuarios:
            if x[0] == usuario and senha == x[1]:
                valido =  True
                break
            else: valido =  False

        if valido == True: return valido
        else: return valido 


if __name__ == "__main__":
    conexao = Conexao.crinado_conexao()

    cursor = conexao.cursor()

    comando = """SELECT ul.usuario, ul.senha FROM usuario_login ul """
    
    tetse = cursor.execute(comando)
    for x in tetse:
        print(x[0], x[1])
