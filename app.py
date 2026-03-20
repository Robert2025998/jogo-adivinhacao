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

if "acertou" not in st.session_state:
    st.session_state.acertou = False

if "ranking" not in st.session_state:
    st.session_state.ranking = []

st.markdown('<div class="titulo">🎯 Adivinhador Nº 1</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Descubra o número secreto e prove que você é o melhor jogador.</div>', unsafe_allow_html=True)

st.markdown('<div class="bloco">', unsafe_allow_html=True)

nome = st.text_input("Digite seu nome")
st.write(f"Tentativas: {st.session_state.tentativas}")

palpite = st.number_input("Digite seu palpite", min_value=1, max_value=10, step=1)

if st.button("Tentar", disabled=st.session_state.acertou):

    if not nome:
        st.warning("Digite seu nome antes de jogar.")
    else:
        st.session_state.tentativas += 1

        if palpite == st.session_state.numero_secreto:
            st.session_state.acertou = True

            st.session_state.ranking.append({
                "nome": nome,
                "tentativas": st.session_state.tentativas
            })

    if palpite == st.session_state.numero_secreto:
        st.session_state.acertou = True
        jogador = nome if nome else "Jogador"

        st.session_state.ranking.append({
            "nome": jogador,
            "tentativas": st.session_state.tentativas
        })

        st.session_state.ranking = sorted(
            st.session_state.ranking,
            key=lambda x: x["tentativas"]
        )[:5]

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

st.markdown('</div>', unsafe_allow_html=True)

st.subheader("🏆 Ranking")

if st.session_state.ranking:
    for i, item in enumerate(st.session_state.ranking, start=1):
        st.write(f"{i}º - {item['nome']} ({item['tentativas']} tentativas)")
else:
    st.write("Nenhum resultado ainda.")
