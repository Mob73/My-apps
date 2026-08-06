import streamlit as st
st.set_page_config(page_title='QUIZ', page_icon='❓', layout='wide')

questions = [{'Q':'Quelle est la capitale du Guatemala?',
             'propositions':['Madrid', 'Flores', 'Guatemala']},
             {'Q':"Quelle est la capitale du Côte d'ivoire?",
             'propositions':['Lomé', 'Abidjan', 'Cocody']},
             {'Q':'Quelle est la capitale du Algérie?',
             'propositions':['Toronto', 'Alger', 'Marrakech']}]
reponses = {0:'Guatemala',
            1:'Abidjan',
            2:'Alger'}

st.title("Mon quiz interactif ")
st.subheader('PAYS ET CAPITALES')

with st.form("questions"):
    reponse_utilisateur = {}
    for i, q in enumerate(questions):
        reponse_utilisateur[i] = st.radio(
            label=q['Q'] ,
            options = q["propositions"],
            key=f'q_{i}')
    btn = st.form_submit_button('Soumettre')
    if btn:
        st.session_state.score = 0
        if reponse_utilisateur == reponses:
            st.write(f'Score : 3/ 3')
            st.write('Félicitations!')
            st.balloons()
        else:
            for i, ans in reponse_utilisateur.items():
                if ans in reponses.get(i):
                    st.session_state.score+=1
            st.write(f'Score : {st.session_state.score} / 3')
            st.write('Vous y êtes presque, reéssayez')

                
