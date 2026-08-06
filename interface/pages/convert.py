import streamlit as st

st.set_page_config('Convertisseur', '🧮', 'wide')
st.title('CONVERTISSEUR DE DONNEES : ')

categorie  = st.selectbox('Catégorie', ['Longueur', 'Poids', 'Temperature'])
valeur = st.number_input('Valeur à convertir', value = 0.0)
unite = st.selectbox('Unité', ['mètre', 'kilomètre', 'gramme', 'kilogramme', 'celsius', 'kelvin'])
btn = st.button('Convertir')
if btn:
    if categorie == 'Longueur' and unite == 'mètre':
        result = valeur*0.001
        st.write(f'Valeur convertie en kilomètre : {result}')
    elif categorie == 'Longueur' and unite == 'kilomètre':
        result = valeur*1000
        st.write(f'Valeur convertie en mètre : {result}')
    elif categorie == 'Poids' and unite == 'gramme':
        result = valeur*0.001
        st.write(f'Valeur convertie en kilogramme : {result}')
    elif categorie == 'Poids' and unite == 'kilogramme':
        result = valeur*1000
        st.write(f'Valeur convertie en gramme : {result}')
    elif categorie == 'Temperature' and unite == 'kelvin':
        result = valeur+273
        st.write(f'Valeur convertie en celsius : {result}')
    elif categorie == 'Temperature' and unite == 'celsius':
        result = valeur-273
        st.write(f'Valeur convertie en kelvin : {result}')
    else:
        st.write("L'unité choisie ne correspond pas à cette catégorie!")
        st.write('Faites correspondres unité et catégorie.')