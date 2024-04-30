#logic
#-----
#welcom message
import streamlit as st
st.title("Welcome to todo webapp!")
todolist_local = []
filepath = 'todolist.txt'


def readfile(todolist_local, filepath):
    with open(filepath, 'r') as file:
        for lines in file:
            todolist_local.append(lines.strip())
    return todolist_local

#initiate readfile so that the todolist is updated with latest data
readfile(todolist_local, filepath)

def write2file(todolist_local, filepath):
    with open(filepath, 'w') as file:
        for item in todolist_local:
            file.writelines(item + '\n')


def add_todo_item():
    todolist_local.append(st.session_state.todo_item)
    write2file(todolist_local,filepath)
    st.session_state.todo_item ='' #clears the input field


#text input
user_todo = st.text_input(label='todo_item',
              placeholder='enter new todo item',
              key='todo_item',
              on_change = add_todo_item
              )

#display from text file all checkbox
for index, items in enumerate(todolist_local):
    checked =  st.checkbox(items, key= index )
    if checked:
        todolist_local.remove(items)
        write2file(todolist_local, filepath)
        st.experimental_rerun()
        #enable rerun so deletion happens instantly else deletion happens after you select next checkbox


