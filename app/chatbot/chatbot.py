from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

router = APIRouter()

context = """
A cidade do Rio de Janeiro disponibiliza uma ampla variedade de serviços municipais essenciais para o bem-estar 
da população, abrangendo áreas como saúde, educação, transporte, limpeza urbana, segurança, assistência social, cultura 
e urbanismo. Na saúde, a Secretaria Municipal de Saúde (SMS) coordena hospitais, unidades de pronto atendimento (UPAs) 
e postos de saúde, além de programas de vacinação e atendimento domiciliar . A educação é gerida pela Secretaria Municipal 
de Educação (SME), responsável por escolas de ensino infantil e fundamental, bem como programas de reforço escolar 
e educação para jovens e adultos . O transporte público é supervisionado pela Secretaria Municipal de Transportes (SMTR), 
que regula ônibus, BRT, VLT, táxis e mototáxis, além de oferecer serviços como o cartão de estacionamento para idosos 
e pessoas com deficiência . A limpeza urbana é realizada pela Companhia Municipal de Limpeza Urbana (Comlurb), 
que cuida da coleta de lixo, limpeza de ruas e praias, e ações de conscientização ambiental . A segurança é reforçada 
pela Guarda Municipal, que protege bens, serviços e instalações municipais . A assistência social é oferecida por meio 
dos Centros de Referência da Assistência Social (CRAS), que atendem pessoas em situação de vulnerabilidade. A cultura é 
promovida pela Secretaria Municipal de Cultura (SMC), que organiza eventos, exposições e atividades culturais . 
O urbanismo é planejado pela Secretaria Municipal de Desenvolvimento Urbano e Licenciamento (SMDU), responsável por 
licenciamento de obras, fiscalização e conservação de espaços públicos . Todos esses serviços são coordenados pela 
Prefeitura do Rio de Janeiro, visando melhorar a qualidade de vida e promover o desenvolvimento sustentável da cidade.
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
