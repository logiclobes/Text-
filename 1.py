import streamlit as st

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Page 1", "Page 2", "Page 3"])

    if page == "Home":
        st.title("Home Page")
        st.write("Welcome to the Home Page")

    elif page == "Page 1":
        st.title("Page 1")
        st.write("Welcome to Page 1")

    elif page == "Page 2":
        st.title("Page 2")
        st.write("Welcome to Page 2")

    elif page == "Page 3":
        st.title("Page 3")
        st.write("Welcome to Page 3")

if __name__ == "__main__":
    main()
