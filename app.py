import streamlit as st
import random

if "numero_secreto" not in st.session_state:
    st.session_state.numero_secreto = random.randint(1, 10)

st.title("Jogo de Adivinhação")
st.write("Tente acertar o número entre 1 e 10")

palpite = st.number_input("Digite seu palpite", min_value=1, max_value=10, step=1)

if st.button("Tentar"):
    if palpite == st.session_state.numero_secreto:
        st.success("Você acertou!")
    elif palpite < st.session_state.numero_secreto:
        st.warning("O número é maior!")
    else:
        st.warning("O número é menor!")
