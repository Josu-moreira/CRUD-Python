from services.cliente_service import ClienteService


class ClienteController:
    def __init__(self):
        self.service = ClienteService()

    def criar_cliente_controller(self, Nome, Email, Cpf, Numero):
        if not all ([Nome, Email, Cpf, Numero]): 
            raise ValueError("Preencha todos os campos")
        
        return self.service.criar_cliente_service(Nome, Email, Cpf, Numero)
    
    def Listar_Clientes_controller(self):
        return self.service.listar_clientes()


