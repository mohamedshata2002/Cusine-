import streamlit as stl
from LLM_backend import food_suggester ,recipe_suggester
stl.title("Resturnant")
user_message = stl.text_input("You: ", key="input")
if Cusine:
    stl.header("bgi food")
    menue_food ="food"
    stl.write("**Menue items**")
    stl.write(menue_food)