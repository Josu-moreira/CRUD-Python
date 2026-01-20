from models.cliente import Cliente
from database.Mysql import connection


class CrudCliente:
    def create(self, db, cliente: Cliente):
        cursor = db.cursor()
        cursor.execute(
            """ 
                INSERT INTO cliente (nome_cliente, email_cliente, cpf_cnpj_cliente, numero)
                VALUES (%s, %s, %s, %s) 
            """,
            (cliente.nome_cliente, cliente.email_cliente, cliente.cpf_cnpj_cliente, cliente.numero),
        )

    def Read_all(self, db):
        cursor = db.cursor()
        cursor.execute(
            """
                 SELECT id_cliente, nome_cliente, email_cliente, cpf_cnpj_cliente, numero
                 FROM cliente  
            """
        )

        rows = cursor.fetchall()
        clientes = []

        for row in rows:
            clientes.append(
                Cliente(
                    id_cliente=row[0],
                    nome_cliente=row[1],
                    email_cliente=row[2],
                    cpf_cnpj_cliente=row[3],
                    numero=row[4]
                )
            )

        return clientes
        

    def Read_with_name(self, db, nome_cliente):
        cursor = db.cursor()
        cursor.execute(
            """
                 SELECT id_cliente, nome_cliente, email_cliente, cpf_cnpj_cliente
                 FROM cliente  
                 WHERE nome_cliente = %s  
            """,
            (nome_cliente,),
        )

        row = cursor.fetchone()
        if row:
            return Cliente(
                id_cliente=row[0],
                nome_cliente=row[1],
                email_cliente=row[2],
                cpf_cnpj_cliente=row[3],
                numero=row[4]
            )
        return None
        

    def Update(self, db, cliente: Cliente):
        cursor = db.cursor()
        cursor.execute(
            """
                UPDATE cliente
                SET nome_cliente = %s, email_cliente = %s, cpf_cnpj_cliente = %s, numero = %s
                WHERE id_cliente = %s
            """,
            (
                cliente.nome_cliente,
                cliente.email_cliente,
                cliente.cpf_cnpj_cliente,
                cliente.numero,
                cliente.id_cliente,
            ),
        )

    def Delete(self, db, cliente: Cliente):
        cursor = db.cursor()
        cursor.execute(
            """
            DELETE FROM cliente
            WHERE id_cliente = %s;
            """,
            (cliente.id_cliente,),
        )

        
