# 📌 Desafio Técnico – Desenvolvedor(a) Back-end Sênior

A Prefeitura do Rio de Janeiro deseja oferecer aos cidadãos uma **API de Carteira Digital**, onde os usuários poderão:

- Armazenar e gerenciar documentos digitais
- Consultar e carregar créditos do transporte público
- Acessar serviços municipais via chatbot

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.10+ com [FastAPI](https://fastapi.tiangolo.com/)
- **Banco de Dados:** PostgreSQL
- **ORM:** SQLAlchemy + Alembic
- **Testes:** Pytest
- **Autenticação:** JWT (Bearer Token)
- **Documentação:** OpenAPI gerada automaticamente pelo FastAPI
- **Controle de Versão:** Git + GitHub
- **CI/CD:** GitHub Actions
- **Conteinerização:** Docker + Docker Compose

---

## ⚙️ Como Rodar o Projeto

### ✅ Pré-requisitos

- Python 3.10+
- Docker e Docker Compose instalados
- Ambiente virtual configurado (`venv`)

### 📦 Passos para Execução

1. **Clone o repositório:**

```bash
git clone https://github.com/gabrielaM0tta/desafio-senior-backend-developer.git
cd desafio-senior-backend-developer
```
2. **Suba o projeto com Docker:**
```bash
docker compose up -d
```
3. **Execute as migrations:**
```bash
alembic upgrade head
```
## ✅ Como Testar

### 🧪 Rodando os testes

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Execute os testes com:

```bash
pytest
```

---

## 🔐 Testando a API

- Verifique se o banco está ativo acessando:  
  [http://localhost:8000/health](http://localhost:8000/health)

- Use a rota de autenticação para obter um **token JWT**
- Com o token em mãos, acesse as demais rotas protegidas

---

## 🌐 Documentação Interativa

Acesse a documentação automática via OpenAPI/Swagger:

👉 [http://localhost:8000/docs#/](http://localhost:8000/docs#/)

---

## 🧠 Decisões Técnicas

### 📌 Arquitetura

- API monolítica, ideal para projetos simples e com prazos curtos
- Utilizado o padrão **Controller - Service - Repository (CSR)** adaptado ao FastAPI, visando maior organização e manutenibilidade
- SQLAlchemy foi escolhido como ORM por oferecer suporte a código síncrono
- Autenticação via **JWT** para proteger rotas

### 📌 Banco de Dados

- PostgreSQL configurado via **Docker Compose**
- Migrações de schema gerenciadas com **Alembic**

### 📌 Testes Automatizados

- Framework de testes: **Pytest**
- Cobertura de funcionalidades principais como:
  - Documentação
  - Passe de transporte
  - Verificação de saúde da API (`/health`)

### 📌 CI/CD

- Pipeline simples com **GitHub Actions**
- Testes executados automaticamente a cada push na branch `main`

---

## 🧩 Modelagem de Banco de Dados

<img width="621" height="371" alt="Screenshot from 2025-07-30 21-34-17" src="https://github.com/user-attachments/assets/48ba79db-0e2f-426b-8e53-a1aee207ab79" />

---

## 💡 Contato

- 📧 E-mail: [gbss.santos1707@gmail.com](mailto:gbss.santos1707@gmail.com)
- 💼 LinkedIn: [Linkedin](https://www.linkedin.com/in/gabrielasantosmotta/)

