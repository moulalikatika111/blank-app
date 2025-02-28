import streamlit as st
import requests
def fetch_pokemon_data(pokemon_identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
import streamlit as st

st.title("Pokémon Info App")


pokemon_input = st.text_input("Enter Pokémon Name or ID:")

if pokemon_input:
    pokemon_data = fetch_pokemon_data(pokemon_input.lower())
            
    if pokemon_data:
        st.image(pokemon_data['sprites']['front_default'], caption=pokemon_data['name'].capitalize())
        st.write(f"**Name:** {pokemon_data['name'].capitalize()}")
                                                                    
        st.write("**Types:**")
        for type_info in pokemon_data['types']:
            st.write(f"- {type_info['type']['name'].capitalize()}")
                                                                                                                                                                        
        st.write("**Stats:**")
        for stat_info in pokemon_data['stats']:
            st.write(f"- {stat_info['stat']['name'].capitalize()}: {stat_info['base_stat']}")
    else:
        st.error("Pokémon not found. Please check the name or ID.")
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
                                                                                                                                                       