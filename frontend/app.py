# frontend/app.py
import streamlit as st
import json
from datetime import datetime, time, date, timedelta
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="MediCare - Assistente Virtual",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
.main-header {
    text-align: center;
    color: #2E86AB;
    padding: 20px 0;
    border-bottom: 2px solid #E8F4FD;
    margin-bottom: 30px;
}

.chat-message {
    padding: 15px;
    margin: 10px 0;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.user-message {
    background-color: #DCF2FF;
    margin-left: 50px;
}

.bot-message {
    background-color: #F0F8F0;
    margin-right: 50px;
}

.info-box {
    background-color: #E8F4FD;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #2E86AB;
    margin: 20px 0;
}

.success-box {
    background-color: #E8F5E8;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #28A745;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# Dados da clínica (simulados)
CLINIC_INFO = {
    "name": "MediCare Clínica Geral",
    "address": "Rua da Saúde, 123 - Centro - São Paulo/SP",
    "phone": "(11) 3456-7890",
    "hours": "Segunda a Sexta: 8h às 18h",
    "insurance": ["SulAmérica", "Bradesco Saúde", "Amil", "Unimed", "NotreDame Intermédica"],
    "private_consultation": "R$ 150,00",
    "doctor": "Dr. Silva - Clínico Geral"
}

# Horários disponíveis (simulados)
def get_available_slots():
    available_slots = []
    today = date.today()
    
    for i in range(1, 8):  # Próximos 7 dias
        current_date = today + timedelta(days=i)
        if current_date.weekday() < 5:  # Segunda a sexta
            slots = ["09:00", "10:30", "14:00", "15:30", "16:30"]
            for slot in slots:
                available_slots.append({
                    "date": current_date,
                    "time": slot,
                    "available": True
                })
    return available_slots

# Inicializar session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "bot",
        "content": "Olá! 👋 Sou o assistente virtual da MediCare. Como posso ajudá-lo hoje?",
        "timestamp": datetime.now()
    })

if "current_flow" not in st.session_state:
    st.session_state.current_flow = "menu"

if "appointment_data" not in st.session_state:
    st.session_state.appointment_data = {}

# Sidebar com informações da clínica
st.sidebar.markdown("### 🏥 MediCare Clínica Geral")
st.sidebar.markdown(f"""
**📍 Endereço:**  
{CLINIC_INFO['address']}

**📞 Telefone:**  
{CLINIC_INFO['phone']}

**⏰ Horários:**  
{CLINIC_INFO['hours']}

**💰 Consulta Particular:**  
{CLINIC_INFO['private_consultation']}

**🏥 Convênios:**
""")

for insurance in CLINIC_INFO['insurance']:
    st.sidebar.markdown(f"• {insurance}")

# Função para processar mensagens
def process_message(user_input):
    responses = {
        # Saudações
        "oi": "Olá! Como posso ajudá-lo?",
        "olá": "Oi! Em que posso ser útil?",
        "bom dia": "Bom dia! Como posso ajudá-lo hoje?",
        "boa tarde": "Boa tarde! Em que posso ajudar?",
        
        # Agendamento
        "agendar": "Perfeito! Vou ajudá-lo a agendar uma consulta. Preciso de algumas informações. Qual seu nome completo?",
        "consulta": "Para agendar uma consulta, preciso do seu nome completo. Pode me informar?",
        
        # Informações
        "horário": f"Funcionamos {CLINIC_INFO['hours']}",
        "endereço": f"Estamos localizados na {CLINIC_INFO['address']}",
        "convenio": f"Aceitamos: {', '.join(CLINIC_INFO['insurance'])}",
        "convênio": f"Aceitamos: {', '.join(CLINIC_INFO['insurance'])}",
        "valor": f"Consulta particular: {CLINIC_INFO['private_consultation']}",
        "preço": f"Consulta particular: {CLINIC_INFO['private_consultation']}",
        
        # Cancelamento
        "cancelar": "Para cancelar uma consulta, preciso do seu nome e telefone. Lembrando que cancelamentos devem ser feitos com 24h de antecedência.",
        
        # Ajuda
        "ajuda": """Posso ajudá-lo com:
        
🗓️ **Agendar consulta**
📞 **Informações da clínica**  
💰 **Valores e convênios**
❌ **Cancelar consulta**
📍 **Endereço e horários**

O que você gostaria de fazer?"""
    }
    
    # Buscar resposta
    user_lower = user_input.lower().strip()
    
    for key, response in responses.items():
        if key in user_lower:
            return response
    
    # Resposta padrão
    return """Desculpe, não entendi sua solicitação. Posso ajudá-lo com:

🗓️ Agendar consulta
📞 Informações da clínica  
💰 Valores e convênios
❌ Cancelar consulta

Digite 'ajuda' para ver todas as opções."""

# Header principal
st.markdown('<h1 class="main-header">🏥 MediCare - Assistente Virtual</h1>', unsafe_allow_html=True)

# Área principal - Chat
st.markdown("### 💬 Chat de Atendimento")

# Container para mensagens
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>Você:</strong> {message["content"]}
                <br><small>{message["timestamp"].strftime("%H:%M")}</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 Assistente:</strong> {message["content"]}
                <br><small>{message["timestamp"].strftime("%H:%M")}</small>
            </div>
            """, unsafe_allow_html=True)

# Input do usuário
col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "Digite sua mensagem:",
        placeholder="Ex: Quero agendar uma consulta",
        key="user_input"
    )

with col2:
    send_button = st.button("Enviar", type="primary", use_container_width=True)

# Processar mensagem
if send_button and user_input:
    # Adicionar mensagem do usuário
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now()
    })
    
    # Processar e adicionar resposta do bot
    bot_response = process_message(user_input)
    st.session_state.messages.append({
        "role": "bot",
        "content": bot_response,
        "timestamp": datetime.now()
    })
    
    # Rerun para atualizar o chat
    st.rerun()

# Botões de ação rápida
st.markdown("---")
st.markdown("### ⚡ Ações Rápidas")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📅 Agendar Consulta", use_container_width=True):
        st.session_state.messages.append({
            "role": "user",
            "content": "Quero agendar uma consulta",
            "timestamp": datetime.now()
        })
        bot_response = process_message("agendar")
        st.session_state.messages.append({
            "role": "bot",
            "content": bot_response,
            "timestamp": datetime.now()
        })
        st.rerun()

with col2:
    if st.button("📍 Endereço", use_container_width=True):
        st.session_state.messages.append({
            "role": "user",
            "content": "Qual o endereço?",
            "timestamp": datetime.now()
        })
        bot_response = process_message("endereço")
        st.session_state.messages.append({
            "role": "bot",
            "content": bot_response,
            "timestamp": datetime.now()
        })
        st.rerun()

with col3:
    if st.button("🏥 Convênios", use_container_width=True):
        st.session_state.messages.append({
            "role": "user",
            "content": "Quais convênios aceitam?",
            "timestamp": datetime.now()
        })
        bot_response = process_message("convenio")
        st.session_state.messages.append({
            "role": "bot",
            "content": bot_response,
            "timestamp": datetime.now()
        })
        st.rerun()

with col4:
    if st.button("💰 Valores", use_container_width=True):
        st.session_state.messages.append({
            "role": "user",
            "content": "Qual o valor da consulta?",
            "timestamp": datetime.now()
        })
        bot_response = process_message("valor")
        st.session_state.messages.append({
            "role": "bot",
            "content": bot_response,
            "timestamp": datetime.now()
        })
        st.rerun()

# Seção de agendamento (simplificada para o MVP)
st.markdown("---")
st.markdown("### 📋 Agendamento Rápido")

with st.expander("Agendar Consulta (Formulário)"):
    with st.form("appointment_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            patient_name = st.text_input("Nome Completo*")
            patient_phone = st.text_input("Telefone*")
            
        with col2:
            patient_email = st.text_input("Email")
            insurance_type = st.selectbox(
                "Tipo de Consulta",
                ["Particular"] + CLINIC_INFO['insurance']
            )
        
        # Horários disponíveis
        available_slots = get_available_slots()[:10]  # Primeiros 10 slots
        
        slot_options = []
        for slot in available_slots:
            slot_str = f"{slot['date'].strftime('%d/%m/%Y')} - {slot['time']}"
            slot_options.append(slot_str)
        
        selected_slot = st.selectbox("Horário Disponível", slot_options)
        
        notes = st.text_area("Observações (opcional)")
        
        if st.form_submit_button("Confirmar Agendamento", type="primary"):
            if patient_name and patient_phone:
                st.markdown(f"""
                <div class="success-box">
                    <h4>✅ Agendamento Confirmado!</h4>
                    <p><strong>Paciente:</strong> {patient_name}</p>
                    <p><strong>Data/Hora:</strong> {selected_slot}</p>
                    <p><strong>Tipo:</strong> {insurance_type}</p>
                    <p><strong>Telefone:</strong> {patient_phone}</p>
                    
                    <hr>
                    
                    <h5>📋 Orientações:</h5>
                    <ul>
                        <li>Chegue 15 minutos antes do horário</li>
                        <li>Traga RG, CPF e carteirinha do convênio</li>
                        <li>Para cancelar, ligue com 24h de antecedência</li>
                    </ul>
                    
                    <p><strong>Em caso de dúvidas, ligue:</strong> {CLINIC_INFO['phone']}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Por favor, preencha pelo menos Nome e Telefone.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>🏥 <strong>MediCare Clínica Geral</strong> | Cuidando da sua saúde com tecnologia</p>
    <p>📞 {phone} | 📍 {address}</p>
    <small>⚡ Powered by AI Assistant | Desenvolvido com ❤️</small>
</div>
""".format(phone=CLINIC_INFO['phone'], address=CLINIC_INFO['address']), 
unsafe_allow_html=True)