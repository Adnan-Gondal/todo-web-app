import streamlit as st
import functions

todos = functions.show_todos()

if "new_todo" not in st.session_state:
    st.session_state.new_todo = ""


def web_add_todo():
    todo = st.session_state["new_todo"]
    if todo:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state.new_todo = ""
        st.rerun()


st.title("Todo App")
st.subheader("Keep track of tasks that need to be performed")
# st.write("More random text")


functions.display_todo_checkbox(todos)


st.text_input(label="label necessary", label_visibility="hidden", placeholder="Add new Todo",
              on_change=web_add_todo(), key="new_todo")


st.session_state