from models.cliente import Cliente
from repositories.cliente_repository import CrudCliente
from database.Mysql import connection
from utils.validators import validar_cpf_cnpj, validar_email

class ClienteService:

    def __init__(self):
        self.Crud = CrudCliente()

    def criar_cliente_service(self, nome, email, cpf_cnpj, numero):

        if not validar_email(email):
            raise ValueError("Email inválido")

        if not validar_cpf_cnpj(cpf_cnpj):
            raise ValueError("CPF/CNPJ inválido")

        novo_cliente = Cliente(
            id_cliente= None,
            nome_cliente= nome,
            email_cliente=email,
            cpf_cnpj_cliente=cpf_cnpj,
            numero=numero
        )

        with connection() as db:
           self.Crud.create(db, novo_cliente)

        return novo_cliente
    

    def listar_clientes(self):
        with connection() as db:
            return self.Crud.Read_all(db)
            
    