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