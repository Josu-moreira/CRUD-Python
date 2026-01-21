# 📦 Projeto CRUD

Este projeto é uma aplicação **CRUD (Create, Read, Update, Delete)** desenvolvida com foco em boas práticas de organização de código, separação de responsabilidades e facilidade de manutenção. Ele permite o gerenciamento de registros em um banco de dados de forma simples e estruturada.

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **MySQL**
* **Tkinter** (interface gráfica)
* **mysql-connector-python**
* **dotenv** (variáveis de ambiente)

---

## 📂 Estrutura do Projeto

```
project-root/
│
├── main.py                # Ponto de entrada da aplicação
├── .env                   # Variáveis de ambiente
│
├── models/                # Entidades (regras de negócio)
│   └── cliente.py
│   └── item.py
|   └── itens_pedido.py
|   └── pedidos.py

├── repository/            # Acesso a dados (SQL)
│   └── cliente_repository.py
│   └── item_repository.py
│   └── itens_pedidos_repository.py
│   └── pedidos_repository.py
│
├── services/              # Regras de negócio e validações
│   └── cliente_service.py
│   └── item_service.py
│   └── itens_pedidos_service.py
│   └── pedidos_service.py
|
├── controller/              # Entradas e saídas da aplicação
│   └── cliente_controller.py
│   └── item_controller.py
│   └── itens_pedidos_controller.py
│   └── pedidos_controller.py
│
├── utils/                 # Funções auxiliares
│   └── formatters.py
│   └── validators.py
│
├── view/             # Interface gráfica (Tkinter)
│   └── TelaCliente.py
│   └── TelaPrincipal.py
│   └── TelaItem.py
│   └── TelaPedidos.py
│
└── README.md
```

> 📌 A estrutura segue uma abordagem inspirada em **MVC**, separando interface, regras de negócio e acesso a dados.

---

## ⚙️ Funcionalidades

* ✅ Criar novos registros
* 🔍 Listar registros cadastrados
* ✏️ Atualizar informações
* ❌ Remover registros
* 📊 Visualização em tabela (Treeview)

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
```

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/Josu-moreira/CRUD-Python.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd seu-repositorio
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate     # Windows
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:

   ```bash
   python main.py
   ```

---

## 🧠 Conceitos Aplicados

* CRUD
* Clean Architecture (adaptada para Python)
* MVC (conceitualmente)
* Context Manager (`with`)
* Separação de responsabilidades

---

## 📌 Próximas Melhorias

* 🔒 Validação avançada de dados
* 📦 Migração para ORM (SQLAlchemy)
* 🧪 Testes automatizados
* 📈 Paginação e filtros
* 🌐 Versão Web (Flask ou FastAPI)

---

## 👤 Autor

**Josué Moreira**
Estudante de Análise e Desenvolvimento de Sistemas
Interesse em Desenvolvimento e Automação

---

## 📄 Licença

Este projeto é de uso educacional e livre para modificações.
