from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

router = APIRouter()

context = """
A Prefeitura do Rio de Janeiro oferece diversos serviços aos cidadãos, como saúde, educação, transporte e limpeza urbana. 
As unidades de saúde estão abertas 24 horas em áreas específicas e os centros de saúde têm horários variados. 
O transporte público é operado pela Prefeitura e pela concessionária de ônibus.
Existem vários programas sociais, como o "Cartão Carioca", que oferece descontos em transporte público. 
Para informações sobre agendamento de consultas ou atendimento de urgência, a Secretaria Municipal de Saúde pode ser consultada diretamente.
O programa de limpeza urbana visa a manutenção e limpeza das ruas, com caminhões especializados que coletam o lixo de várias áreas da cidade.
A educação é oferecida gratuitamente pela rede pública de ensino municipal, com escolas em várias regiões.
"""

class Question(BaseModel):
    ask: str

def question_process(ask: str) -> str:
    try:
        response = qa_pipeline(question=ask, context=context)
        return response.get("answer", "Desculpe, não consegui encontrar uma resposta.")
    except Exception as e:
        return "Houve um problema ao processar sua pergunta. Tente novamente mais tarde."


@router.post("/")
def chatbot_router(question: Question):
    ask = question.ask
    response = question_process(ask)
    return {"resposta": response}
