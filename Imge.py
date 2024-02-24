import streamlit as st
import re
from PIL import Image

def text_to_binary(text):
    binary_result = ''.join(format(ord(char), '08b') for char in text)
    return binary_result

def encode_lsb(image_file, message,password):
     if len(password) < 4:
        st.error("Password must be at least 4 characters long")
        return
     image = Image.open(image_file)
     message +="W@E"

     binary_message = text_to_binary(message)
     binary_message += "1111111111111110"  # Adding a sentinel value to indicate the end of the message

     if len(binary_message) > image.size[0] * image.size[1]:
        st.error("Message is too long to be encoded in the image")
        return

     index = 0
     for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = list(image.getpixel((i, j)))

            for k in range(3):  # Iterate over RGB channels
                if index < len(binary_message):
                    pixel[k] = pixel[k] & ~1 | int(binary_message[index])
                    index += 1

            image.putpixel((i, j), tuple(pixel))

     output_path = "encoded_image.png"
     image.save(output_path)
     st.success("Message encoded successfully")

def decode_lsb(encoded_image_file,password):
    try:
        image = Image.open(encoded_image_file)
        binary_message = ""
        
        
        for i in range(image.size[0]):
         for j in range(image.size[1]):
            pixel = list(image.getpixel((i, j)))

            for k in range(3):  # Iterate over RGB channels
                binary_message += str(pixel[k] & 1)

        binary_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        decoded_message = ''.join([chr(int(byte, 2)) for byte in binary_message])

        end_index = decoded_message.find("1111111111111110")
        if end_index != -1:
          decoded_message = decoded_message[:end_index]
        
        return decoded_message
    except:
        st.error("Error")

def encode_message(image_file, message, password):
    if image_file == "":
        st.error("Please select an image file")
        return

    if message == "":
        st.error("Please enter a message to encode")
        return

    if len(password) < 4:
        st.error("Password must be at least 4 characters long")
        return

    encode_lsb(image_file, message, password)
    
def decode_message(encoded_image_file, password):
    if encoded_image_file == "":
        st.error("Please select an encoded image file")
        return
    
    if len(password) < 4:
        st.error("Password must be at least 4 characters long")
        return

    decoded_message = decode_lsb(encoded_image_file,password)
    decodeValue=splitdecodemessage(decoded_message)
    if decoded_message:
        st.success(f"The hidden message is: {decodeValue}")        
    else:
        st.error("No hidden message found in the image.")

def splitdecodemessage(string):
    result = []
    result=string.split("W@E")
    return result[0]

# Streamlit UI setup
st.title("Image Steganography")

image_file = st.file_uploader("Select Image File:", type=["png", "jpg", "jpeg"])
message = st.text_input("Enter Message:")
password = st.text_input("Enter Password:", type="password")

if st.button("Encode"):
    encode_message(image_file, message, password)

if st.button("Decode"):
    decode_message(image_file, password)
