# Importando as bibliotecas
from tkinter import* 
from tkinter import Tk , StringVar , ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog as fd


from PIL import Image, ImageTk

from datetime import date

from view import *

import os




# Cores Para Aplicar---------------------------------------------

co0 = "#2e2d2b" #preto
co1 = "#feffff" #branco
co2 = "#4fa882" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" # -profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # +verde
co9 = "#e9edf5" # +verde
co10 = "#000000" #PRETO

# Janela 

janela = Tk()
janela.title('Best Clothes')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


# Criação De Frames

frameCima = Frame(janela,width=1043,height=50,bg=co1,relief=FLAT)
frameCima.grid(row=0,column=0)

frameMeio = Frame(janela,width=1043,height=303,bg=co1,pady=20,relief=FLAT)
frameMeio.grid(row=1,column=0, pady=1,padx=0,sticky=NSEW)

frameBaixo = Frame(janela,width=1043,height=300,bg=co1,relief=FLAT)
frameBaixo.grid(row=2,column=0, pady=0,padx=1,sticky=NSEW)


# Criando Funcoes---------------------------------------
global tree

# Função Adicionar

def inserir():
    global imagem, imagem_string , l_imagem

    nome = e_nome.get()
    estoque= e_estoque.get()
    fornecedor = e_fornecedor.get()
    telefone_fornecedor = e_telfornecedor.get()
    data = e_calendar.get() 
    valor = e_valor.get()
    descricao = e_descricao.get()
    imagem = imagem_string

    lista_inserir = [nome , estoque , fornecedor , telefone_fornecedor , data , valor, descricao , imagem]
    
    for i in lista_inserir:
       if i == '':

          messagebox.showerror('Erro','Preencha todos os dados')
          return
    
    inserir_form (lista_inserir)

    messagebox.showinfo('Sucesso' , 'Os dados foram inseridos com Sucesso')

    e_nome.delete(0,'end')
    e_estoque.delete(0,'end')
    e_fornecedor.delete(0,'end')
    e_telfornecedor.delete(0,'end')
    e_calendar.delete(0,'end')
    e_valor.delete(0,'end')
    e_descricao.delete(0,'end')
    

    mostrar()
   


 # Funcao Escolher imagem 
global imagem, imagem_string , l_imagem

# Função Atualizar
def atualizar():
   global imagem, imagem_string , l_imagem
   try:
     treev_dados = tree.focus()
     treev_dicionario = tree.item(treev_dados)
     treev_lista = treev_dicionario['values']

     valor = treev_lista[0]
    
     e_nome.delete(0,'end')
     e_estoque.delete(0,'end')
     e_fornecedor.delete(0,'end')
     e_telfornecedor.delete(0,'end')
     e_calendar.delete(0,'end')
     e_valor.delete(0,'end')
     e_descricao.delete(0,'end')
     
     id = int(treev_lista[0])
     e_nome.insert(0,treev_lista[1])
     e_estoque.insert(0,treev_lista[2])
     e_fornecedor.insert(0,treev_lista[3])
     e_telfornecedor.insert(0,treev_lista[4])
     e_calendar.insert(0,treev_lista[5])
     e_valor.insert(0,treev_lista[6])
     e_descricao.insert(0,treev_lista[7])
     imagem_string = treev_lista[8]
     

     def update ():
        global imagem, imagem_string , l_imagem
        
        nome = e_nome.get()
        estoque= e_estoque.get()
        fornecedor = e_fornecedor.get()
        telefone_fornecedor = e_telfornecedor.get()
        data = e_calendar.get() 
        valor = e_valor.get()
        descricao = e_descricao.get()
        imagem = imagem_string

        

        if imagem == '':
            imagem =  e_descricao.insert(0,treev_lista[7])


        lista_atualizar = [nome , estoque , fornecedor , telefone_fornecedor , data , valor, descricao , imagem ,id]

        for i in lista_atualizar:
           if i =='':
              messagebox.showerror('Erro' , 'Preencha todos os campos')
              return
           
        atualizar_form (lista_atualizar)
        messagebox.showinfo('Sucesso' , 'Produto atualizado com sucesso')


        e_nome.delete(0,'end')
        e_estoque.delete(0,'end')
        e_fornecedor.delete(0,'end')
        e_telfornecedor.delete(0,'end')
        e_calendar.delete(0,'end')
        e_valor.delete(0,'end')
        e_descricao.delete(0,'end')
           
        b_confirmar.destroy()

        mostrar()

   

     b_confirmar = Button(frameMeio,command=update , width=13,text='Confirmar'.upper() ,overrelief=RIDGE ,font=('Ivy 8 bold'), bg=co2 , fg=co1)
     b_confirmar.place(x=330,y=185)
        
                 
        
        
        
        
   except IndexError:
     messagebox.showerror('Erro' , 'Selecione um produto para atualizar')
        
        
        
        
# Função Deletar
     
def deletar():
   try:
     treev_dados = tree.focus()
     treev_dicionario = tree.item(treev_dados)
     treev_lista = treev_dicionario['values']

     valor = treev_lista[0]

     deletar_form([valor])

     messagebox.showinfo('Sucesso' , 'Produto deletados com Sucesso')
     
     mostrar()

        
   except IndexError:
    messagebox.showerror('Erro' , 'Selecione um produto para Deletar')
        
                
        

def escolher_imagem():
   global imagem, imagem_string , l_imagem

   imagem = fd.askopenfilename()
   imagem_string = imagem

 # Função Abrir a imagem  
   imagem = Image.open(imagem)
   imagem = imagem.resize((170,170))
   imagem = ImageTk.PhotoImage(imagem)

   l_imagem = Label(frameMeio,image=imagem, compound=LEFT , relief=RAISED, bg=co1 , fg=co4)
   l_imagem.place(x=700,y=10)
   


# Função Abrir Imagem do Produto
def ver_imagem ():
   global imagem, imagem_string , l_imagem
   
   treev_dados = tree.focus()
   treev_dicionario = tree.item(treev_dados)
   treev_lista = treev_dicionario['values']

   valor = [int(treev_lista[0])]

   item  = ver_item(valor)
   
   imagem = item[0][8]

   # Abrindo a Imagem DNV
   imagem = Image.open(imagem)
   imagem = imagem.resize((170,170))
   imagem = ImageTk.PhotoImage(imagem)

   l_imagem = Label(frameMeio,image=imagem, bg=co1 , fg=co4)
   l_imagem.place(x=700,y=10)





# Logo
app_img = Image.open('BC.png')
app_img = app_img.resize((60,60))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima,image=app_img , text=' Gerenciamento De Estoque ' , width=900 , compound=LEFT , relief=RAISED ,anchor=NW , font=('Verdana 20 bold'), bg=co1 , fg=co4)
app_logo.place(x=0,y=0)



      


# Customizando FrameMeio--------------------------------


# Criando Entradas
l_nome = Label(frameMeio,text='Nome' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_nome.place(x=10,y=10)
e_nome = Entry(frameMeio , width=30 , justify='left', relief=SOLID)
e_nome.place(x=130,y=11)


l_estoque = Label(frameMeio,text='Estoque' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_estoque.place(x=10,y=40)
e_estoque = Entry(frameMeio , width=30 , justify='left', relief=SOLID)
e_estoque.place(x=130,y=41)


l_fornecedor = Label(frameMeio,text='Fornecedor' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_fornecedor.place(x=10,y=70)
e_fornecedor= Entry(frameMeio , width=30 , justify='left', relief=SOLID)
e_fornecedor.place(x=130,y=71)


l_telfornecedor = Label(frameMeio,text='Tell Fornecedor' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_telfornecedor.place(x=10,y=100)
e_telfornecedor = Entry(frameMeio , width=30 , justify='left', relief=SOLID)
e_telfornecedor.place(x=130,y=101)

l_calendar = Label(frameMeio,text='Data Chegada' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_calendar.place(x=10,y=130)
e_calendar = DateEntry(frameMeio , width=12 ,Background='darkblue' ,bordewidth=2,year=2024)
e_calendar.place(x=130,y=131)

l_valor = Label(frameMeio,text='Valor' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_valor.place(x=10,y=160)
e_valor = Entry(frameMeio , width=30 , justify='left', relief=SOLID)
e_valor.place(x=130,y=161)


l_descricao = Label(frameMeio,text='Descrição' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_descricao.place(x=10,y=190)
e_descricao = Entry(frameMeio , width=30 , justify='left', relief=SOLID)
e_descricao.place(x=130,y=191)

# Criando os Botoes--------------------------------------------------------

# Botao Carregar
l_carregar = Label(frameMeio,text='Imagem Produto' , height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1 , fg=co4)
l_carregar.place(x=10,y=220)
b_carregar = Button(frameMeio,command=escolher_imagem, width=30,text='Carregar'.upper() ,compound=CENTER ,anchor=CENTER,overrelief=RIDGE ,font=('Ivy 8 '), bg=co1 , fg=co0)
b_carregar.place(x=130,y=221)


# Botao Adicionar

img_add = Image.open('adicionarr.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_adicionar = Button(frameMeio,command=inserir,  image=img_add, width=95,text='  Adicionar'.upper() ,compound=LEFT ,anchor=NW,overrelief=RIDGE ,font=('Ivy 8 '), bg=co1 , fg=co0)
b_adicionar.place(x=330,y=10)


# Botao Atualizar

img_updt = Image.open('atualizar.png')
img_updt = img_updt.resize((20,20))
img_updt = ImageTk.PhotoImage(img_updt)

b_update = Button(frameMeio,command=atualizar ,image=img_updt, width=95,text='  Atualizar'.upper() ,compound=LEFT ,anchor=NW,overrelief=RIDGE ,font=('Ivy 8 '), bg=co1 , fg=co0)
b_update.place(x=330,y=50)


# Botao Deletar

img_del = Image.open('deletar.png')
img_del = img_del.resize((20,20))
img_del = ImageTk.PhotoImage(img_del)

b_update = Button(frameMeio,command=deletar ,image=img_del, width=95,text='  Deletar'.upper() ,compound=LEFT ,anchor=NW,overrelief=RIDGE ,font=('Ivy 8 '), bg=co1 , fg=co0)
b_update.place(x=330,y=90)

# Ver o Produto

img_prod = Image.open('produtos.png')
img_prod = img_prod.resize((20,20))
img_prod= ImageTk.PhotoImage(img_prod)

b_prod = Button(frameMeio, command=ver_imagem ,image=img_prod, width=95,text='  Ver produto'.upper() ,compound=LEFT ,anchor=NW,overrelief=RIDGE ,font=('Ivy 7 '), bg=co1 , fg=co0)
b_prod.place(x=330,y=221)


# Label Total

l_total = Label(frameMeio,text='' ,width=14 ,height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co10 , fg=co1)
l_total.place(x=450,y=17)
l_total_ = Label(frameMeio,text='    Valor Total Dos Produtos      '  ,height=1, anchor=NW, font=('Ivy 10 bold'), bg=co10 , fg=co1)
l_total_.place(x=450,y=12)

# Label Quantidade

l_quant = Label(frameMeio,text='' ,width=14 ,height=2, anchor=CENTER, pady=5  ,font=('Ivy 17 bold'), bg=co10 , fg=co1)
l_quant.place(x=450,y=90)
l_quant_ = Label(frameMeio,text='    Quantidade De Produtos'  ,height=1, anchor=NW, font=('Ivy 10 bold'), bg=co10 , fg=co1)
l_quant_.place(x=450,y=92)


# Tabela------------------------------------------

def mostrar():

 global tree
 
 tabela_head = ['#ID','Nome',  'Estoque','Fornecedor', 'Telefone Fornecedor', 'Data da compra','Valor do Produto', 'descrição']
 lista_itens = ver_form()




 tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

#Barra Vertical
 vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

#Barra Horizontal
 hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

 tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
 tree.grid(column=0, row=0, sticky='nsew')
 vsb.grid(column=1, row=0, sticky='ns')
 hsb.grid(column=0, row=1, sticky='ew')
 frameBaixo.grid_rowconfigure(0, weight=12)

 hd=["center","center","center","center","center","center","center", 'center']
 h=[40,150,100,160,130,100,100, 100]
 n=0

 for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # Ajustando a largura da tabela
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1


# Inserindo os itens dentro da tabela
 for item in lista_itens:
    tree.insert('', 'end', values=item)


 quantidade = []

 for iten in lista_itens:
    quantidade.append(item[6])

 Total_valor = sum(quantidade)
 Total_itens = len(quantidade)

 l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
 l_quant['text'] = Total_itens


mostrar()

janela.mainloop()
