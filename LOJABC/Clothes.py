# importando o sqlite
import sqlite3 as lite

# Criando a conexão com o banco de dados
con = lite.connect('dados.db')

# Criando as Tabelas
with con:
    cur= con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT , nome TEXT , estoque TEXT, fornecedor TEXT , telefone_fornecedor TEXT , data DATE, valor DECIMAL, descricao TEXT , imagem TEXT)")


