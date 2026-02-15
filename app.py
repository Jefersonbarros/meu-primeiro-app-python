import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu App Python", page_icon="🐍")

# Título e texto
st.title("Olá do Python na Web! 🌐")
st.write("Este site foi construído inteiramente em Python.")

# Entrada de dados do usuário
nome = st.text_input("Qual é o seu nome?")

# Botão e lógica simples
if st.button("Clique aqui"):
    if nome:
        st.success(f"Bem-vindo, {nome}! Você acaba de rodar um script Python no navegador.")
        st.balloons() # Sim, ele tem efeitos visuais prontos!
    else:
        st.warning("Por favor, digite seu nome primeiro.")

# Um gráfico simples para mostrar o poder dos dados
st.subheader("Exemplo de Gráfico Nativo")
st.line_chart([10, 25, 40, 35, 50])