import streamlit as st

st.set_page_config(
    page_title="Carte de visite",
    page_icon="📇",
    layout="wide"
)
with st.sidebar:
    st.title("Mes Applis")
    st.divider()
    st.caption("Version 1.0")
# Définition des pages avec des chemins relatifs depuis la racine
visit_card = st.Page("pages/visit_card.py", title="Carte de visite", icon="📇")
quiz = st.Page("pages/quiz.py", title="Quiz", icon="❓")
convert = st.Page('pages/convert.py', title = 'Convertisseur', icon='🧮')
calculatrice = st.Page('pages/calculatrice.py', title='Calculatrice', icon='➕')
data = st.Page('pages/data_explorer.py', title='Data Explorer', icon='🔢')

# Configuration de la navigation
pg = st.navigation([visit_card, quiz, convert, calculatrice, data])

# Exécution de la page sélectionnée
pg.run()
