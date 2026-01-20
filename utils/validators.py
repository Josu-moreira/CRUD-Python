import re

def validar_email(email: str) -> bool:
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf_cnpj(documento: str) -> bool:
    documento = re.sub(r"\D", "", documento)
    return len(documento) in (11, 14)