import pandas as pd 
import streamlit as st


st.set_page_config('Explorateur de fichier csv', layout = 'wide')
st.title("Explorateur de fichier csv")
file = st.file_uploader('Importez un fichier CSV', 'csv')
if file is not None:
    df = pd.read_csv(file)
    st.write(df.describe())
    st.dataframe(df)
else :
    st.write('Ajouter un fichier CSV pour afficher ses caractéristiques.')