import streamlit as st


# Classe do Portfólio
class Portfolio:

    def __init__(self, nome, github, email, whatsapp, endereco):
        self.nome = nome
        self.github = github
        self.email = email
        self.whatsapp = whatsapp
        self.endereco = endereco
        # self.imagem = imagem

    # Método para exibir informações
    def exibir_portfolio(self):

        st.title("💼 Meu Portfólio")

        # st.image(self.imagem, width=200)

        st.header(self.nome)

        st.write("### 👨‍💻 Sobre Mim")
        st.write(
            "Sou estudante de programação apaixonado por tecnologia e desenvolvimento de sistemas."
        )

        st.write("### 🔗 GitHub")
        st.write(self.github)

        st.write("### 📧 Email")
        st.write(self.email)

        st.write("### 📱 WhatsApp")
        st.write(self.whatsapp)

        st.write("### 📍 Endereço")
        st.write(self.endereco)


# Criando objeto
meu_portfolio = Portfolio(
    nome="Murilo Santos",
    github="https://github.com/Murilosvic",
    email="ms6247948@gmail.com",
    whatsapp="(11) 945299408",
    endereco="Rua orestes barbosa 280, guarulhos",
    

)

# Exibir portfólio
meu_portfolio.exibir_portfolio()