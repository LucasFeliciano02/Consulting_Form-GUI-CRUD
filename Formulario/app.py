"""
pip install tkcalendar
"""

"""
Cabeleraria: Nomes e seus nomes tem horarios, das 9 h as 19h da noita, do lado colocam o nome da pessoa que contratou o serviço
"""

"""
* COLOCAR DOUTOR NO PROCURAR NOME, PARA PODER PROCURAR POR NOME E POR DOUTOR
"""


# Criando conexao

import sqlite3 as lite
from tkinter import *
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image  # Pillow
from tkinter import ttk
from tkinter import messagebox


conexao = lite.connect('Formulario_bd.db')


# * FAZENDO CRUD NO BANCO DE DADOS

## Create = Criar/Inserir

"""
with conexao:
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE Formularios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, email TEXT, telefone TEXT, nascimento DATE, sexo TEXT, data_consulta DATE, estado_consulta TEXT, especialidade TEXT, doutor TEXT, horario TEXT, Informacao_extra TEXT)")
"""

# Inserindo informações


def inserir_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO Formularios(nome, cpf, email, telefone, nascimento, sexo, data_consulta, estado_consulta, especialidade, doutor, horario, Informacao_extra) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, i)


# * Read = Mostrando informações da tabela

def mostrar_info(nome=None):
    lista = []

    with conexao:
        cursor = conexao.cursor()
        selector = f"WHERE nome = '{nome}'" if nome else ''
        query = f"SELECT * FROM Formularios {selector}"
        cursor.execute(query)
        informacao = cursor.fetchall()

        for i in informacao:
            lista.append(i)

    return lista


def atualizar_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE Formularios SET nome=?, cpf=?, email=?, telefone=?, nascimento=?, sexo=?, data_consulta=?, estado_consulta=?, especialidade=?, doutor=?, horario=?, Informacao_extra=? WHERE id=?"
        cursor.execute(query, i)


def deletar_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM Formularios WHERE id=?"
        cursor.execute(query, i)


# cores
cor0 = "#f0f3f5"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
cor5 = "#e06636"   # - profit
cor6 = "#038cfc"   # azul
cor7 = "#ef5350"   # vermelha
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # sky blue


# * ----- Criando Janela -----

janela = Tk()
janela.title('Formulario')
# janela.geometry('1043x453')
janela.configure(bg=cor9)
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('consultoria.ico')  # icon do app


style = ttk.Style(janela)
style.theme_use('clam')


# * ----- Dividindo a janela em Frames -----

frame_cima = Frame(janela, width=310, height=50, bg=cor6, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=300, height=718, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=598, height=770, bg=cor1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


# * Imagem

img = Image.open('consultoria.png')
img = img.resize((40, 40), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT,
                 padx=10, relief='flat', anchor='nw', bg=cor6)
app_logo.place(x=240, y=4)


# *----- Configurando frame_cima com o nome do app -----

app_nome = Label(frame_cima, text='Formulário do Consultorio',
                 anchor=NW, font=('Ivy 13 bold'), bg=cor6, fg=cor1, relief='flat')
app_nome.place(x=10, y=17)


# * Variaveis globais

global tree


# * Função inserir

def inserir():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    nascimento = entry_nascimento.get()
    sexo = combo_sexo.get()
    data_consulta = entry_calendario.get()
    estado_consulta = combo_estado.get()
    especialidade = combo_especialidade.get()
    doutor = combo_doutores.get()
    horario = combo_horario.get()
    Informacao_extra = entry_sobre.get()

    lista = [nome, cpf, email, telefone, nascimento, sexo, data_consulta,
             estado_consulta, especialidade, doutor, horario, Informacao_extra]

    if nome == '' or cpf == '' or email == '' or telefone == '':
        messagebox.showwarning('Atenção!', 'Preencha todos os campos')
    else:
        inserir_info(lista)
        messagebox.showinfo(
            'Sucesso!', 'Os novos dados foram inseridos com sucesso')

        entry_nome.delete(0, 'end')
        entry_cpf.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_nascimento.delete(0, 'end')
        combo_sexo.delete(0, 'end')
        entry_calendario.delete(0, 'end')
        combo_estado.delete(0, 'end')
        combo_especialidade.delete(0, 'end')
        combo_doutores.delete(0, 'end')
        combo_horario.delete(0, 'end')
        entry_sobre.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()


# * Função atualizar

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        entry_nome.delete(0, 'end')
        entry_cpf.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        entry_nascimento.delete(0, 'end')
        combo_sexo.delete(0, 'end')
        entry_calendario.delete(0, 'end')
        combo_estado.delete(0, 'end')
        combo_especialidade.delete(0, 'end')
        combo_doutores.delete(0, 'end')
        combo_horario.delete(0, 'end')
        entry_sobre.delete(0, 'end')

        entry_nome.insert(0, tree_lista[1])
        entry_cpf.insert(0, tree_lista[2])
        entry_email.insert(0, tree_lista[3])
        entry_telefone.insert(0, tree_lista[4])
        entry_nascimento.insert(0, tree_lista[5])
        combo_sexo.insert(0, tree_lista[6])
        entry_calendario.insert(0, tree_lista[7])
        combo_estado.insert(0, tree_lista[8])
        combo_especialidade.insert(0, tree_lista[9])
        combo_doutores.insert(0, tree_lista[10])
        combo_horario.insert(0, tree_lista[11])
        entry_sobre.insert(0, tree_lista[12])

        def update():
            nome = entry_nome.get()
            cpf = entry_cpf.get()
            email = entry_email.get()
            telefone = entry_telefone.get()
            nascimento = entry_nascimento.get()
            sexo = combo_sexo.get()
            data_consulta = entry_calendario.get()
            estado_consulta = combo_estado.get()
            especialidade = combo_especialidade.get()
            doutor = combo_doutores.get()
            horario = combo_horario.get()
            Informacao_extra = entry_sobre.get()

            lista = [nome, cpf, email, telefone, nascimento, sexo, data_consulta,
                     estado_consulta, especialidade, doutor, horario, Informacao_extra, valor_id]

            if nome == '':
                messagebox.showwarning(
                    'Atenção!', 'Primeiro é necessario selecionar um item da tabela e atualizar para depois confirmar')
            else:
                atualizar_info(lista)
                messagebox.showinfo(
                    'Sucesso!', 'Os dados foram atualizados com sucesso')

                entry_nome.delete(0, 'end')
                entry_cpf.delete(0, 'end')
                entry_email.delete(0, 'end')
                entry_telefone.delete(0, 'end')
                entry_nascimento.delete(0, 'end')
                combo_sexo.delete(0, 'end')
                entry_calendario.delete(0, 'end')
                combo_estado.delete(0, 'end')
                combo_especialidade.delete(0, 'end')
                combo_doutores.delete(0, 'end')
                combo_horario.delete(0, 'end')
                entry_sobre.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

                botao_confirmar.destroy()

            mostrar()

        # botao atualizar
        botao_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, anchor=NW, font=(
            'Ivy 7 bold'), bg='#0f944d', fg='#ffffff', relief='raised', overrelief='ridge')
        botao_confirmar.place(x=118, y=685)

    except IndexError:
        messagebox.showerror(
            'Erro!', 'Selecione um dos dados da tabela para poder atualizar')


# Função atualizar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso!', 'Os dados foram deletados com sucesso')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror(
            'Erro!', 'Selecione um dos dados da tabela para poder deletar')


# * ----- Configurando frame_baixo com labels e entrys.... -----

# Label e entry do NOME

label_nome = Label(frame_baixo, text='Nome completo:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_nome.place(x=10, y=10)

entry_nome = Entry(frame_baixo, width=45, justify='left',
                   relief='solid', highlightthickness=1)
entry_nome.place(x=14, y=40)


# * Label e entry do CPF

def format_cpf(event=None):

    text = entry_cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for index in range(len(text)):

        if not text[index] in "0123456789":
            continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    entry_cpf.delete(0, "end")
    entry_cpf.insert(0, new_text)


entry_cpf = Entry(frame_baixo, width=45, justify='left',
                  relief='solid', highlightthickness=1)
entry_cpf.place(x=14, y=105)
entry_cpf.bind("<KeyRelease>", format_cpf)


label_cpf = Label(frame_baixo, text='CPF:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_cpf.place(x=10, y=75)


# Label e entry do EMAIL

label_email = Label(frame_baixo, text='Email:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_email.place(x=10, y=140)

entry_email = Entry(frame_baixo, width=45, justify='left',
                    relief='solid', highlightthickness=1)
entry_email.place(x=14, y=170)


# * Label, entry E FORMATAÇÃO do TELEFONE

def format_tel(event=None):

    text = entry_telefone.get().replace(".", "").replace("-", "")[:16]
    new_text = " ("

    if event.keysym.lower() == "backspace":
        return

    for index in range(len(text)):

        if not text[index] in "0123456789":
            continue

        if index in [0]:
            new_text += text[index] + "("
        elif index in [3]:
            new_text += text[index] + ") "
        elif index == 6:
            new_text += text[index] + " "
        elif index == 11:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    entry_telefone.delete(0, "end")
    entry_telefone.insert(0, new_text)


entry_telefone = Entry(frame_baixo, width=45, justify='left',
                       relief='solid', highlightthickness=1)
entry_telefone.place(x=14, y=235)
entry_telefone.bind("<KeyRelease>", format_tel)


label_telefone = Label(frame_baixo, text='Telefone:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_telefone.place(x=10, y=205)


# Label e entry do NASCIMENTO

label_nascimento = Label(frame_baixo, text='Data nascimento:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_nascimento.place(x=10, y=267)

entry_nascimento = DateEntry(
    frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022, font=('Ivy 10'))
entry_nascimento.place(x=14, y=295)


# Label e Combobox de SEXO

sexos = ['M', 'F', 'Outro']

label_sexo = Label(frame_baixo, text='Sexo:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_sexo.place(x=200, y=267)

# Combobox

combo_sexo = ttk.Combobox(frame_baixo, width=8,
                          justify=CENTER, font=('Ivy 10'))

combo_sexo.place(x=190, y=295)

combo_sexo['values'] = (sexos)


# Label e entry do DATA DA CONSULTA

label_calendario = Label(frame_baixo, text='Data da Consulta:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_calendario.place(x=10, y=335)

entry_calendario = DateEntry(
    frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022, font=('Ivy 10'))
entry_calendario.place(x=14, y=365)


# Label e entry do STATUS DA CONSULTA

status = ['Em processo', 'Terminado']

label_estado = Label(frame_baixo, text='Status da consulta:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_estado.place(x=160, y=335)

# Combobox

combo_estado = ttk.Combobox(
    frame_baixo, width=14, justify=CENTER, font=('Ivy 10'))

combo_estado.place(x=173, y=366)

combo_estado['values'] = (status)


# Label e Combobox do ESPECIALIDADE

profissoes = ['Cardiologia', 'Dermatologia', 'Nutrição', 'Pediatria',
              'Oftalmologia', 'Psiquiatria', 'Ortopedia', 'Endocrinologia']

label_especialidade = Label(frame_baixo, text='Especialidade:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_especialidade.place(x=10, y=405)

# Combobox

combo_especialidade = ttk.Combobox(
    frame_baixo, width=12, justify=CENTER, font=('Ivy 10'))

combo_especialidade.place(x=14, y=435)

combo_especialidade['values'] = (profissoes)


# Label e Combobox do DOUTOR

Profissionais = ['Carlos-CARDIOLOGISTA', 'Json da silva-DERMATOLOGISTA',
                 'Ereníce Toreto-NUTRICIONISTA', 'Róbson Silvano da Silva Sauro-PEDIATRA', 'Reynaldo-OFTALMOLOGISTA', 'Arlindo Feio-PSIQUIATRA', 'Suélen karamasovsk-ORTOPEDISTA', 'Reginaldo Rossi-ENDOCRINOLOGISTA']

label_doutores = Label(frame_baixo, text='Profissional:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_doutores.place(x=107, y=475)

# Combobox

combo_doutores = ttk.Combobox(
    frame_baixo, width=37, justify=CENTER, font=('Ivy 10'))

combo_doutores.place(x=14, y=505)

combo_doutores['values'] = (Profissionais)


# Label e entry do HORARIO

horarios = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30',
            '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30']

label_horario = Label(frame_baixo, text='Horário da consulta:', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_horario.place(x=162, y=405)

# Combobox

combo_horario = ttk.Combobox(
    frame_baixo, width=10, justify=CENTER, font=('Ivy 10'))

combo_horario.place(x=184, y=436)

combo_horario['values'] = (horarios)


# Label e entry do INFORMAÇÃO EXTRA

label_sobre = Label(frame_baixo, text='Informação Extra: (Campo opcional)', anchor=NW, font=(
    'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
label_sobre.place(x=11, y=544)

entry_sobre = Entry(frame_baixo, width=45, justify='left',
                    relief='solid', highlightthickness=1)
entry_sobre.place(x=14, y=576)


# * FUNÇÃO procurar dados e ver dados

def procurar():
    nome = entry_pesquisar.get()

    lista = mostrar_info(nome)

    tree.delete(*tree.get_children())

    for item in lista:
        tree.insert('', 'end', values=item)

    entry_pesquisar.delete(0, 'end')


# BOTAO PROCURAR NOME

entry_pesquisar = Entry(frame_baixo, width=20, justify='left',
                        relief='solid', highlightthickness=1)
entry_pesquisar.place(x=163, y=611)


botao_pesquisar = Button(frame_baixo, command=procurar, text='Procurar nome/Ver dados:', width=22, anchor=NW, font=(
    'Verdana 7 bold'), bg='white', fg='black', relief='raised', overrelief='ridge')
botao_pesquisar.place(x=14, y=611)


# * ----- Botões -----

# Botão inserir

botao_inserir = Button(frame_baixo, command=inserir, text='Adicionar', width=10, anchor=NW, font=(
    'Ivy 9 bold'), bg=cor6, fg=cor1, relief='raised', overrelief='ridge')
botao_inserir.place(x=16, y=650)


# Botão Atualizar

botao_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, anchor=NW, font=(
    'Ivy 9 bold'), bg=cor2, fg=cor1, relief='raised', overrelief='ridge')
botao_atualizar.place(x=112, y=650)


# Botão Deletar

botao_deletar = Button(frame_baixo, command=deletar, text='Deletar', width=10, anchor=NW, font=(
    'Ivy 9 bold'), bg=cor7, fg=cor1, relief='raised', overrelief='ridge')
botao_deletar.place(x=208, y=650)


# * ------------------- codigo para tabela Frame Direita ----------------

def mostrar():

    global tree

    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID', 'nome', 'cpf', 'E-mail', 'telefone', 'nascimento', 'Sexo',
                   'Consulta', 'Status', 'Especialidade', 'Doutor', 'Horário', 'Extra']

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended",
                        columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center",
          "nw", "nw", "nw", "nw", "center", "center"]
    h = [25, 195, 90, 175, 85, 75, 50, 70, 80, 100, 186, 50, 80]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


# Chamando a função mostrar

mostrar()


# * Centralizando o arquivo


# Dimensoes da janela
largura = 1590
altura = 770

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2.02 - largura/2
posy = altura_screen/5 - altura/2.65

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()
