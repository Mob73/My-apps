import streamlit as st

with st.sidebar:
    st.title("Mes Applis")
    st.divider()
    st.caption("Version 1.0")

st.set_page_config(
    page_title="Carte de visite",
    page_icon="📇",
    layout="wide"
)

# Définition des pages avec des chemins relatifs depuis la racine
visit_card = st.Page("visit_card.py", title="Carte de visite", icon="📇")
quiz = st.Page("quiz.py", title="Quiz", icon="❓")
convert = st.Page('convert.py', title = 'Convertisseur', icon='🧮')
calculatrice = st.Page('calculatrice.py', title='Calculatrice', icon='➕')
data = st.Page('data_explorer.py', title='Data Explorer', icon='🔢')

# Configuration de la navigation
pg = st.navigation([visit_card, quiz, convert, calculatrice, data])

# Exécution de la page sélectionnée
pg.run()
