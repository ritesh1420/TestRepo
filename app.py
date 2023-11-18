# app.py
import streamlit as st

def main():
    # Set page title and icon
    st.set_page_config(page_title="My Streamlit Web Page", page_icon=":rocket:")

    # Add content to the page
    st.title("Welcome to My Streamlit Web Page")
    st.write("This is a basic example of a Streamlit web page.")
    st.write("Feel free to customize and add more content!")

if __name__ == "__main__":
    main()
