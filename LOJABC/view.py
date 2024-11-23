# importando sqlite3
import sqlite3 as lite

# Criando a conexão

con = lite.connect('dados.db')
dados = []
 
# Inserindo os Dados

def inserir_form(i):
  with con:
    cur = con.cursor()
    query = "INSERT INTO  inventario(nome , estoque , fornecedor , telefone_fornecedor , data , valor, descricao  , imagem) VALUES (?,?,?,?,?,?,?,?)"
    cur.execute(query, i)

 
 # Atualizando os Dados
          
def atualizar_form(i):
  with con:
    cur = con.cursor()
    query = "UPDATE  inventario SET nome=? , estoque=? , fornecedor=? , telefone_fornecedor=? , data=? , valor=?, descricao= ? , imagem=? WHERE id=?"
    cur.execute(query, i)    

# Deletando os Dados

def deletar_form(i):
   with con:
    cur = con.cursor()
    query = "DELETE FROM inventario WHERE id=?"
    cur.execute(query,i)    

# Mostrando os Dados

def ver_form():
   ver_dados = []
   with con:
    cur = con.cursor()
    query = "SELECT * FROM inventario"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)
    return ver_dados
 
def ver_item(id):
    ver_dados_indiv = []
    with con:
     cur = con.cursor()
     query = "SELECT * FROM inventario WHERE id=?"
     cur.execute(query , id)

     rows = cur.fetchall()
     for row in rows:
      ver_dados_indiv.append(row)
     
    return ver_dados_indiv
 

