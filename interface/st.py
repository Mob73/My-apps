import streamlit as st
st.set_page_config(page_icon='😁', page_title='MOB', layout='wide')
st.title('Hello, World!')
#nom = st.text_input('nom', 'Anne')
#if nom.strip().lower() == 'moubarak':
 #   st.balloons()
#elif nom.strip().lower() == 'stan':
#    st.snow()

#age = st.number_input('Age', min_value=17, max_value=25)

btn = st.button('play')
is_first = True
if 'is_first' not in st.session_state :
    st.session_state.is_first = True

if btn:
    if st.session_state.is_first:
        st.snow()
        st.session_state.is_first = False
    else:
        st.balloons()
        st.session_state.is_first = True



