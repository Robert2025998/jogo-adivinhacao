import streamlit as st
import random

st.set_page_config(page_title="Adivinhador Nº 1", page_icon="🎯", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #080c1a 0%, #141b3a 100%);
    color: white;
}

.titulo {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-top: 10px;
    margin-bottom: 5px;
    text-shadow: 0 0 10px rgba(120, 160, 255, 0.8);
}

.subtitulo {
    text-align: center;
    font-size: 18px;
    color: #cfd8ff;
    margin-bottom: 30px;
}

.bloco {
    background-color: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 0 20px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 10)

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

st.markdown('<div class="titulo">🎯 Adivinhador Nº 1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Descubra o número secreto e prove que você é o melhor jogador.</div>', unsafe_allow_html=True)

st.markdown('<div class="bloco">', unsafe_allow_html=True)

palpite = st.number_input("Digite seu palpite", min_value=1, max_value=10, step=1)

if st.button("Tentar"):
    st.session_state.tentativas += 1

    if palpite == st.session_state.numero_secreto:
        st.success(f"🔥 Vitória! Você acertou em {st.session_state.tentativas} tentativa(s).")
    elif palpite < st.session_state.numero_secreto:
        st.warning("⬆️ O número secreto é maior.")
    else:
        st.warning("⬇️ O número secreto é menor.")

if st.button("Jogar novamente"):
    st.session_state.numero_secreto = random.randint(1, 10)
    st.session_state.tentativas = 0
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
