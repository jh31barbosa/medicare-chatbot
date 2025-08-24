# 🏥 MediCare ChatBot Assistant

> Assistente virtual inteligente para automação de atendimento em clínicas médicas

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.0.340+-orange.svg)](https://langchain.com)

## 📋 Sobre o Projeto

O **MediCare ChatBot** é um assistente virtual desenvolvido para automatizar o atendimento de clínicas médicas, oferecendo:

- ✅ **Agendamento automático** de consultas 24/7
- ✅ **Informações instantâneas** sobre a clínica
- ✅ **Gestão de convênios** e valores
- ✅ **Interface amigável** e responsiva
- ✅ **Integração com IA** para conversação natural

## 🚀 Funcionalidades

### 🤖 Chat Inteligente
- Conversação natural em português
- Respostas contextualizadas
- Escalation para atendimento humano

### 📅 Sistema de Agendamentos
- Verificação de horários disponíveis
- Agendamento com validação automática
- Confirmação por email/SMS
- Gestão de cancelamentos

### 📊 Informações da Clínica
- Horários de funcionamento
- Endereço e localização
- Convênios aceitos
- Valores de consultas
- Orientações médicas básicas

## 🛠️ Tecnologias Utilizadas

### Backend
- **FastAPI** - API REST moderna e rápida
- **LangChain** - Framework para aplicações com IA
- **OpenAI GPT** - Modelo de linguagem para conversação
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL/SQLite** - Banco de dados

### Frontend
- **Streamlit** - Interface web interativa
- **HTML/CSS** - Customização visual
- **JavaScript** - Funcionalidades dinâmicas

### IA & ML
- **OpenAI API** - Processamento de linguagem natural
- **ChromaDB** - Banco de dados vetorial
- **Embeddings** - Busca semântica em documentos

## 📦 Instalação

### Pré-requisitos
- Python 3.8+
- Pip
- Git

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/medicare-chatbot.git
cd medicare-chatbot
```

2. **Crie o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas chaves de API
```

5. **Execute a aplicação**
```bash
streamlit run frontend/app.py
```

6. **Acesse no navegador**
```
http://localhost:8501
```

## ⚙️ Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# API Keys
OPENAI_API_KEY=your-openai-api-key-here

# Database
DATABASE_URL=sqlite:///./medicare.db

# App Settings
ENVIRONMENT=development
DEBUG=True

# Clinic Settings
CLINIC_NAME=MediCare Clínica Geral
CLINIC_PHONE=(11) 3456-7890
CLINIC_ADDRESS=Rua da Saúde, 123 - Centro - São Paulo/SP
```

## 📁 Estrutura do Projeto

```
medicare_chatbot/
├── 📁 api/                    # FastAPI backend
│   ├── main.py               # Aplicação principal
│   ├── routes/               # Endpoints da API
│   └── models/               # Modelos de dados
├── 📁 ai/                     # Módulos de IA
│   ├── langchain_setup.py    # Configuração LangChain
│   ├── embeddings.py         # Base de conhecimento
│   └── chat_agent.py         # Lógica do chatbot
├── 📁 frontend/               # Interface Streamlit
│   ├── app.py               # App principal
│   └── components/          # Componentes reutilizáveis
├── 📁 database/               # Banco de dados
│   ├── connection.py        # Conexão
│   └── models.py           # Modelos SQLAlchemy
├── 📁 knowledge_base/         # Documentos para IA
│   ├── clinic_info.txt      # Informações da clínica
│   └── faqs.txt            # Perguntas frequentes
├── requirements.txt          # Dependências Python
├── .env                     # Variáveis de ambiente
└── README.md               # Este arquivo
```

## 🎯 Roadmap

### ✅ Fase 1 - MVP (Concluída)
- [x] Interface básica com Streamlit
- [x] Chat funcional com respostas pré-definidas
- [x] Sistema de agendamento simples
- [x] Deploy local

### 🚧 Fase 2 - IA Integration (Em desenvolvimento)
- [ ] Integração com OpenAI GPT
- [ ] Base de conhecimento com embeddings
- [ ] Conversação natural
- [ ] Melhorias na UX

### 📋 Fase 3 - Features Avançadas (Planejado)
- [ ] Banco de dados completo
- [ ] Sistema de notificações
- [ ] Dashboard administrativo
- [ ] Integração WhatsApp

### 🚀 Fase 4 - Produção (Futuro)
- [ ] Deploy em nuvem
- [ ] Monitoramento e logs
- [ ] Testes automatizados
- [ ] Documentação da API

## 🧪 Como Testar

### Cenários de Teste

1. **Agendamento Básico**
   - Digite: "Quero agendar uma consulta"
   - Siga o fluxo de agendamento
   - Verifique confirmação

2. **Informações da Clínica**
   - Teste: "Qual o endereço?"
   - Teste: "Quais convênios aceitam?"
   - Teste: "Qual o horário de funcionamento?"

3. **Cancelamento**
   - Digite: "Quero cancelar minha consulta"
   - Siga as instruções


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Seu Nome**
- GitHub: [@jh31barbosa](https://github.com/jh31barbosa)
- LinkedIn: [José Henrique](https://linkedin.com/in/jh29-dev)
- Email: jh29.dev@gmail.com



