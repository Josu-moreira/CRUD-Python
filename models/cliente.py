class Cliente:
    def __init__(self, nome_cliente, email_cliente, cpf_cnpj_cliente, numero, id_cliente=None):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente
        self.cpf_cnpj_cliente = cpf_cnpj_cliente
        self.numero = numero
