import streamlit as st
import os
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is fun and challenging.",
    "Artificial Intelligence is shaping the future.",
    "Keep calm and code on.",
]

encrypted_message = ""
decrypted_message = ""
password = ""  # Initialize password variable

def encryption(msg, sentences):
    global encrypted_message
    randsen = random.choice(sentences)
    encrypted_message = randsen
    return randsen

def decryption(decmsg):
    global encrypted_message, decrypted_message
    if decmsg.strip() == encrypted_message.strip():
        decrypted_message = message
    else:
        decrypted_message = "Decryption failed."
    return decrypted_message

def decrypt(entered_password, decmsg):
    global decrypted_message
    if entered_password == password:
        decrypted_message = decryption(decmsg) 
        st.text_area("Decrypted Message", decrypted_message)
    elif entered_password == "":
        st.error("Enter Password")
    else:
        st.error("Invalid Password")

def encrypt(entered_password, message):
    global encrypted_message
    if entered_password == password:
        encrypted_message = encryption(message, sentences) 
        st.text_area("Encrypted Message", encrypted_message)
    elif entered_password == "":
        st.error("Enter Password")
    else:
        st.error("Invalid Password") 

def set_password(new_password):
    global password
    if new_password:
        password = new_password
        st.info("Password has been set successfully.")
    else:
        st.error("Please enter a valid password.")

def main():
    st.title("PctApp")
    st.sidebar.header("Options")

    option = st.sidebar.selectbox("Select Option", ["Encrypt", "Decrypt"])

    if option == "Encrypt":
        st.subheader("Encryption")
        message = st.text_area("Enter Message for Encryption", height=100)
        entered_password = st.text_input("Enter Password", type="password")
        if st.button("Encrypt"):
            encrypt(entered_password, message)

    elif option == "Decrypt":
        st.subheader("Decryption")
        decmsg = st.text_area("Enter Encrypted Message", height=100)
        entered_password = st.text_input("Enter Password", type="password")
        if st.button("Decrypt"):
            decrypt(entered_password, decmsg)

    if st.sidebar.button("Set Password"):
        new_password = st.sidebar.text_input("Enter New Password", type="password")
        set_password(new_password)

if __name__ == "__main__":
    main()
