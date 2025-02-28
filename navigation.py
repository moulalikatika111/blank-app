import streamlit as st

if 'current_id' not in st.session_state:
    st.session_state.current_id = 1

col1, col2 = st.columns(2)

with col1:
    if st.button("Previous"):
        if st.session_state.current_id > 1:
            st.session_state.current_id -= 1
            pokemon_data = fetch_pokemon_data(st.session_state.current_id)
            st.experimental_rerun()

with col2:
    if st.button("Next"):
        if st.session_state.current_id < 898:  # Assuming 898 is the last Pokémon ID
            st.session_state.current_id += 1
            pokemon_data = fetch_pokemon_data(st.session_state.current_id)
            st.experimental_rerun()