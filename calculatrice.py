import streamlit as st

import streamlit as st
st.set_page_config('Calculatrice', '➕', 'wide')
st.title('CALCULATRICE')
n1 = st.number_input('Entrez le premier numéro : ')
n2 = st.number_input('Entrez le second numéro')
st.write("Choisissez l'opératiton à effectuer :")
ope = st.selectbox('Opérations', ['addition', 'soustraction', 'multiplication', 'division'])
btn = st.button('Calculer')
if btn :
    if ope == 'addition':
        st.write(f'Résultat : {round(n1+n2, 3)}')
    elif ope == 'soustraction':
        st.write(f'Résultat : {round(n1-n2, 3)}')
    elif ope == 'multiplication':
        st.write(f'Résultat : {round(n1*n2, 3)}')
    elif ope == 'division':
        if n2 == 0:
            st.warning("Attention il n'est pas possible de diviser un nombre par 0")
        else:
            st.write(f'Résultat : {round(n1/n2, 3)}')