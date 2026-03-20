import streamlit as st
import random
from supabase import create_client

st.set_page_config(page_title="Adivinhador Nº 1", page_icon="🎯", layout="centered")

# conexão com Supabase
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 10)

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

if "acertou" not in st.session_state:
    st.session_state.acertou = False

st.title("🎯 Adivinhador Nº 1")

nome = st.text_input("Digite seu nome")
st.write(f"Tentativas: {st.session_state.tentativas}")

palpite = st.number_input("Digite seu palpite", min_value=1, max_value=10, step=1)

if st.button("Tentar", disabled=st.session_state.acertou):
    st.session_state.tentativas += 1

    if palpite == st.session_state.numero_secreto:
        st.session_state.acertou = True
        jogador = nome if nome else "Jogador"

        # salva no banco online
        supabase.table("ranking").insert({
            "nome": jogador,
            "tentativas": st.session_state.tentativas
        }).execute()

        st.success(f"🔥 {jogador}, você acertou em {st.session_state.tentativas} tentativa(s).")

    elif palpite < st.session_state.numero_secreto:
        st.warning("⬆️ O número secreto é maior.")
    else:
        st.warning("⬇️ O número secreto é menor.")

if st.button("Jogar novamente"):
    st.session_state.numero_secreto = random.randint(1, 10)
    st.session_state.tentativas = 0
    st.session_state.acertou = False
    st.rerun()

st.subheader("🏆 Ranking Online")

try:
    resposta = supabase.table("ranking").select("*").order("tentativas").limit(10).execute()
    ranking = resposta.data

    if ranking:
        for i, item in enumerate(ranking, start=1):
            st.write(f"{i}º - {item['nome']} ({item['tentativas']} tentativas)")
    else:
        st.write("Nenhum resultado ainda.")
except Exception:
    st.write("Não foi possível carregar o ranking.")
