
from fastapi import FastAPI
from database import supabase
from pydantic import BaseModel
from datetime import date


# Modelo dos dados do membro
class Membro(BaseModel):
    nome: str
    nascimento: date
    valor_contribuicao: float
    vencimento: int


# Modelo dos dados do pagamento
class Pagamento(BaseModel):
    membro_id: int
    valor: float
    data: date
    pago: bool


# Configuração da API
app = FastAPI(
    title="API Grupo dos Homens",
    description="Sistema de gerenciamento do grupo de Upabuçu",
    version="1.0.0"
)


# Rota inicial
@app.get("/")
def inicio():
    return {
        "mensagem": "API do Grupo dos Homens está funcionando!"
    }


# Verificar se a API está online
@app.get("/status")
def status():
    return {
        "status": "online"
    }


# Listar membros
@app.get("/membros")
def listar_membros():
    try:
        resposta = supabase.table("membros").select("*").execute()

        return {
            "total": len(resposta.data),
            "membros": resposta.data
        }

    except Exception as e:
        return {
            "erro": str(e)
        }


# Cadastrar membro
@app.post("/membros")
def cadastrar_membro(membro: Membro):
    resposta = supabase.table("membros").insert(
        membro.model_dump(mode="json")
    ).execute()

    return {
        "mensagem": "Membro cadastrado com sucesso!",
        "membro": resposta.data
    }


# Cadastrar pagamento
@app.post("/pagamentos")
def cadastrar_pagamento(pagamento: Pagamento):
    dados = {
        "membro_id": pagamento.membro_id,
        "valor_pago": pagamento.valor,
        "data_pagamento": pagamento.data.isoformat(),
        "data": pagamento.data.isoformat(),
        "pago": pagamento.pago
    }

    resposta = supabase.table("pagamentos").insert(
        dados
    ).execute()

    return {
        "mensagem": "Pagamento cadastrado com sucesso!",
        "pagamento": resposta.data
    }


# Listar pagamentos
@app.get("/pagamentos")
def listar_pagamentos():
    resposta = supabase.table("pagamentos").select("*").execute()

    return {
        "total": len(resposta.data),
        "pagamentos": resposta.data
    }
