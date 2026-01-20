import tkinter as tk
from view.TelaCliente import TelaCliente

abas = ["Cliente", "Itens", "Pedidos"]

class JanelaInicial():
    def __init__(self):
        super().__init__()

        self.IniciarJanela()
        self.Frames()
        self.Textos()
        self.Buttons()
        self.JanelaPrincipal.mainloop()

    def IniciarJanela(self):
        self.JanelaPrincipal = tk.Tk()
        self.JanelaPrincipal.title("CRUD com tkinter")
        self.JanelaPrincipal.configure(background="#000000")
        self.JanelaPrincipal.geometry("800x400")
        self.JanelaPrincipal.minsize(800, 400)
        self.JanelaPrincipal.maxsize(1000, 500)

        self.JanelaPrincipal.resizable(True, True)

    def Frames(self):        
        self.JanelaPrincipal.columnconfigure(0, weight=1) 
        self.JanelaPrincipal.columnconfigure(1, weight=1)
        self.JanelaPrincipal.rowconfigure(0, weight=1)

        #CONTAINER PRINCIPAL
        self.container = tk.Frame(self.JanelaPrincipal, bg="#000000")
        self.container.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=1)
        self.container.columnconfigure(2, weight=1)
        self.container.rowconfigure(0, weight=1)

        #LADO DIREITO
        self.frame_direito = tk.Frame(self.container, bg="#09090b")
        self.frame_direito.grid(row=0, column=1, columnspan=2 , sticky="nsew", padx=5, pady=5)
        self.frame_direito.grid_propagate(False)
        self.frame_direito.columnconfigure(0, weight=1)
        self.frame_direito.rowconfigure(0, weight=1)


        #LADO ESQUERDO
        self.frame_esquerdo = tk.Frame(self.container, bg="#09090b")
        self.frame_esquerdo.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.frame_esquerdo.grid_propagate(False)
        self.frame_esquerdo.columnconfigure(0, weight=1)
        self.frame_esquerdo.rowconfigure(0, weight=1)
        self.frame_esquerdo.rowconfigure(1, weight=2)
        self.frame_esquerdo.rowconfigure(2, weight=1)
        
        #TITULO
        self.frame_titulo = tk.Frame(self.frame_esquerdo, bg="#09090b")
        self.frame_titulo.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=20, pady=20)
        self.frame_titulo.columnconfigure(0, weight=1)
        self.frame_titulo.rowconfigure(0, weight=1)

        #ABA DE BOTÕES
        self.frame_button = tk.Frame(self.frame_esquerdo, bg="#09090b")
        self.frame_button.grid(row=1, column=0, rowspan=1, sticky="nsew", padx=20, pady=0)
        self.frame_button.columnconfigure(0,weight=1)
        for i in range(len(abas)):
            self.frame_button.rowconfigure(i, weight=1)

        #PERFIL
        self.frame_perfil= tk.Frame(self.frame_esquerdo, bg="#09090b")
        self.frame_perfil.grid(row=2, column=0, rowspan=1, sticky="nsew", padx=20, pady=20)

    def Textos(self):
        self.Texto_titulo = tk.Label(self.frame_titulo, text="OFFICE",  font=("Georgia", 30), fg="#a855f7", bg="#09090B")
        self.Texto_titulo.grid(row=0, column=0, sticky="nsew", padx=10)

    def Buttons(self):

        for i, nome in enumerate(abas):
            self.Button = tk.Button(self.frame_button, text=nome,  fg="white", bg="#3f3f46", width=10, font=("Arial", 12), command=getattr(self, nome))
            self.Button.grid(column=0, row=i, sticky="ew", padx=(30,30))

    def Cliente(self):
        self.Tela_cliente = TelaCliente(self.frame_direito)
        self.Tela_cliente.grid(column=0 ,row=0, sticky="nsew", padx=20, pady=20)
        self.Tela_cliente.columnconfigure(0, weight=1)
        self.Tela_cliente.rowconfigure(0, weight=1)
        self.Tela_cliente.tkraise()
    
    def Itens(self):
        pass

    def Pedidos(self):
        pass