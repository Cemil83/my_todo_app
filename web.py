import streamlit as st
from streamlit import session_state

import functions

st.title("My Todo App")
st.subheader("This is my todo app")

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+ "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.text_input(label="Enter a todo:",placeholder="Add new todo..",
              on_change=add_todo,key="new_todo")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del session_state[todo]
        st.rerun()