import tkinter as tk
from view.StyleTreeview import aplicar_estilo
from tkinter import ttk
from controller.cliente_controller import ClienteController

Entradas = ["Nome, Email, CPF"]

class TelaCliente(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#000000")

        self.controller = ClienteController() 
        self.Lista = self.controller.Listar_Clientes_controller()

        aplicar_estilo()
        self.criar_frames()
        self.criar_barra()
        # self.mostrar_clientes()  
        self.mostrar_clientes2()

    def criar_frames(self):
        #Frame inteiro
        self.frame_cliente = tk.Frame(self, bg="black")
        self.frame_cliente.grid(column=0, row=0, sticky="nsew")
        self.frame_cliente.columnconfigure(0, weight=1)
        self.frame_cliente.rowconfigure(0, weight=1, minsize=50)
        self.frame_cliente.rowconfigure(1,weight=2, minsize=200)

        #Frame para a barra de pesquisa
        self.frame_pesquisa = tk.Frame(self.frame_cliente, bg="#09090b")
        self.frame_pesquisa.grid(column=0, row=0, sticky="nsew")
        self.frame_pesquisa.rowconfigure(0, weight=1)
        for i in range(7):
             self.frame_pesquisa.columnconfigure(i, weight=1)

        #Frame para o conteúdo
        self.frame_conteudo = tk.Frame(self.frame_cliente, bg="#09090b")
        self.frame_conteudo.grid(column=0, row=1, sticky="nsew")
        self.frame_conteudo.columnconfigure(0, weight=1)
        self.frame_conteudo.rowconfigure(0, weight=1)

        #Frame para o Formulário
        self.frame_forms = tk.Frame(self.frame_conteudo, bg="#09090b")
        self.frame_forms.grid(column=0, row=0, sticky="nsew")
        self.frame_forms.columnconfigure(0, weight=1)
        self.frame_forms.columnconfigure(1,weight=2)

        for i in range(8):
             self.frame_forms.rowconfigure(i, weight=1)



    #Conteúdo da barra  de pesquisa
    def criar_barra(self):
        #Titulo
        self.TituloAba = tk.Label(self.frame_pesquisa, text="Clientes",  font=("Segoe UI", 15, "bold"), fg="white", bg="#09090B")
        self.TituloAba.grid(column=0, row=0, sticky="nsew")

        #Pesquisa
        self.BarraPesquisa = tk.Entry(self.frame_pesquisa, text="Digite aqui", fg="white", bg="#71717a")
        self.BarraPesquisa.grid(column=1, row=0, columnspan=3, sticky="ew" , ipady=3, padx=(0,10))

        #Botão para criar
        self.BtnPesquisa = tk.Button(self.frame_pesquisa, text="Pesquisar", bg="#a855f7")
        self.BtnPesquisa.grid(column=4, row=0, sticky="ew", columnspan=2, pady=(2,0), padx=(0,10))

        self.BtnCriarNovo = tk.Button(self.frame_pesquisa, text="+ Novo", bg="#a855f7", command=lambda:self.mostrar_tela(self.frame_forms))
        self.BtnCriarNovo.grid(column=6, row=0, sticky="ew", columnspan=2, pady=(2,0))

    #Conteúdo do formulário
    def criar_formulário(self):
        #Nome
        self.TituloNome = tk.Label(self.frame_forms, text="Nome:", bg="#09090b",fg="#71717a", font=("Georgia", 10, "bold"))
        self.TituloNome.grid(row=0, column=0, sticky="sw", padx=30)

        self.NomeCliente = tk.Entry(self.frame_forms, bg="#71717a", fg="white")
        self.NomeCliente.grid(row=1, column=0, columnspan=2, sticky="ew", padx=30, ipady=3)

        #Email
        self.TituloEmail =tk.Label(self.frame_forms, text="Email:", bg="#09090b", fg="#71717a", font=("Georgia", 10, "bold"))
        self.TituloEmail.grid(row=2, column=0, sticky="sw", padx=30)

        self.EmailCliente = tk.Entry(self.frame_forms, bg="#71717a")
        self.EmailCliente.grid(row=3, column=0, columnspan=2, sticky="ew", padx=30, ipady=3)

        #CPF
        self.TituloCpf = tk.Label(self.frame_forms, text="CPF/CNPJ:", bg="#09090b", fg="#71717a" , font=("Georgia", 10, "bold"))
        self.TituloCpf.grid(row=4, column=0, sticky="sw", padx=30)

        self.CpfCliente = tk.Entry(self.frame_forms, bg="#71717a")
        self.CpfCliente.grid(row=5, column=0, columnspan=2, sticky="ew", padx=30, ipady=3)

        #NUMERO
        self.TituloCpf = tk.Label(self.frame_forms, text="NUMERO:", bg="#09090b", fg="#71717a" , font=("Georgia", 10, "bold"))
        self.TituloCpf.grid(row=6, column=0, sticky="sw", padx=30)

        self.NumeroCliente = tk.Entry(self.frame_forms, bg="#71717a")
        self.NumeroCliente.grid(row=7, column=0, columnspan=2, sticky="ew", padx=30, ipady=3)

        #Botão de Enviar
        self.EnviarCliente = tk.Button(self.frame_forms, text="Criar Cliente",command=self.criar_cliente,bg="#a855f7")
        self.EnviarCliente.grid(row=8, column=1, pady=(10,0))

        self.CancelarCliente = tk.Button(self.frame_forms, text="Cancelar") 
        self.CancelarCliente.grid(row=8, column=0, pady=(10,0))

    #Conteúdo de todos os clientes
    # def mostrar_clientes(self):
    #     self.Frame_mostrar_cliente = tk.Frame(self.frame_conteudo, bg="#09090b")
    #     self.Frame_mostrar_cliente.grid(column=0, row=0, sticky="nsew")

    #     for i in range(8):
    #         self.Frame_mostrar_cliente.rowconfigure(i, weight=1)
    #     for i in range(4):
    #         self.Frame_mostrar_cliente.columnconfigure(i, weight=1)

    #     for i, nome in enumerate(self.Lista):
    #         self.ListaClientes = tk.Label(self.Frame_mostrar_cliente, text=nome.nome_cliente, bg="#09090b", fg="#71717a", font=("Georgia", 10, "bold"))
    #         self.ListaClientes.grid(row=i, column=0, columnspan=1, sticky="ew", padx=10, ipady=3)

    #     for i, nome in enumerate(self.Lista):
    #         self.ListaClientes = tk.Label(self.Frame_mostrar_cliente, text=nome.email_cliente, bg="#09090b", fg="#71717a", font=("Georgia", 10, "bold"))
    #         self.ListaClientes.grid(row=i, column=1, columnspan=1, sticky="ew", padx=10, ipady=3)

    #     for i, nome in enumerate(self.Lista):
    #         self.ListaClientes = tk.Label(self.Frame_mostrar_cliente, text=nome.cpf_cnpj_cliente, bg="#09090b", fg="#71717a", font=("Georgia", 10, "bold"))
    #         self.ListaClientes.grid(row=i, column=2, columnspan=1, sticky="ew", padx=10, ipady=3)

    def mostrar_clientes2(self):
        self.tv = ttk.Treeview(self.frame_conteudo,columns=("Nome", "Email", "Numero"), show="headings", style="Custom.Treeview")
        self.tv.column("Email", minwidth=0, width=50)
        self.tv.column("Nome", minwidth=0, width=50)
        self.tv.column("Numero", minwidth=0, width=50)
        self.tv.heading("Nome", text="Nome")
        self.tv.heading("Email", text="Email")
        self.tv.heading("Numero", text="Numero")
        self.tv.grid(row=0, column=0, sticky="nsew", pady=(10,0))

        for i in self.Lista:
            self.tv.insert("", "end", values=(i.nome_cliente, i.email_cliente, i.cpf_cnpj_cliente))

    #Função de criar os clientes
    def criar_cliente(self):
            self.controller.criar_cliente_controller(
                self.NomeCliente.get(), self.EmailCliente.get(), self.CpfCliente.get(), self.NumeroCliente.get()
            )       
    
    def mostrar_tela(self, Frame):
        Frame.tkraise()
        self.criar_formulário()
         