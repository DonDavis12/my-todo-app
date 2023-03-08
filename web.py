#in streamlit order of writing the script important.
#streamlit run web.py
#pip freeze > requirements.txt

import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"     #specific object type of streamlit, looks like dictionary
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "", placeholder = "Add new todo....",
              on_change = add_todo, key = "new_todo")