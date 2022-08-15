import string
import streamlit as st
import pandas as pd


def caesarCipher_encode(msg, k):
    '''
    Encode text message using Caesar cipher
    :param
    msg(str): Text input message
    :param
    k(int): Amount of shift position of the characters
    :return
    encrypted_msg(str): Encrypted text message
    '''
    alphabet = string.ascii_lowercase
    map_char = {}
    encrypted_msg = ""
    if not k > 0:
        return "Key should be greater than 0"
    if k > 25:
        if k % 26 >= 0:
            k = k % 26
    for i in range(len(alphabet)):
        map_char[alphabet[i]] = i
    for character in msg:
        if character.isalpha():
            character = character.lower()
            if map_char[character] + k > 25:
                off_k = k - (25 - map_char[character]) - 1
                encrypted_msg += alphabet[off_k]
            else:
                encrypted_msg += alphabet[map_char[character] + k]
        else:
            encrypted_msg += character
    for i in range(len(msg)):
        if msg[i].isalpha():
            if msg[i].isupper():
                encrypted_msg = encrypted_msg[:i] + encrypted_msg[i].upper() + encrypted_msg[i + 1:]

    return encrypted_msg


def caesarCipher_decode(en_msg, k):
    '''
    Decode encrypted Caesar cipher message
    :param
    en_msg(str): Encrypted input message
    :param
    k(int): Amount of shift position of the characters
    :return
    decrypted_msg(str): Original message after decryption
    '''
    alphabet = string.ascii_lowercase
    map_char = {}
    decrypted_msg = ""
    if not k > 0:
        return "Key should be greater than 0"
    if k > 25:
        if k % 26 >= 0:
            k = k % 26
    for i in range(len(alphabet)):
        map_char[alphabet[i]] = i
    for character in en_msg:
        if character.isalpha():
            character = character.lower()
            if map_char[character] - k < 0:
                off_k = 26 - abs(map_char[character] - k)
                decrypted_msg += alphabet[off_k]
            else:
                decrypted_msg += alphabet[map_char[character] - k]
        else:
            decrypted_msg += character
    for i in range(len(en_msg)):
        if en_msg[i].isalpha():
            if en_msg[i].isupper():
                decrypted_msg = decrypted_msg[:i] + decrypted_msg[i].upper() + decrypted_msg[i + 1:]

    return decrypted_msg


def get_cypher_table(k):
    '''
    Get transformation table of Caesar cypher, which is plain alphabet mapped to cypher alphabet
    :param
    k(int): Amount of shift position of the characters
    :return
    p_cypher(dict): Dictionary representing transformation table
    '''
    alphabet = string.ascii_uppercase
    map_char = {}
    p_cypher = {
        "Plain": "Cypher"
    }
    if not k > 0:
        return "Key should be greater than 0"
    if k > 25:
        if k % 26 >= 0:
            k = k % 26
    for i in range(len(alphabet)):
        map_char[alphabet[i]] = i
    for character in alphabet:
        if map_char[character] + k > 25:
            off_k = k - (25 - map_char[character]) - 1
            p_cypher[character] = alphabet[off_k]
        else:
            p_cypher[character] = alphabet[map_char[character] + k]

    return p_cypher


def st_ui():
    '''
    Render the User Interface of the application endpoints
    '''
    st.title("Caesar Message Encryption")
    message = st.text_input(label='Message', placeholder="Type your message")
    k1 = st.number_input('Key', min_value=1, step=1)
    encrypted_msg = caesarCipher_encode(message, k1)
    st.subheader("Encrypted Message")
    st.write(f"**{encrypted_msg}**")
    encrypted_msg = st.text_input(label='Encrypted Message', placeholder="Type your encrypted message")
    k2 = st.number_input('Encryption Key', min_value=1, step=1)
    decrypted_msg = caesarCipher_decode(encrypted_msg, k2)
    st.subheader("Decrypted Message")
    st.write(f"**{decrypted_msg}**")
    st.subheader("Cypher Table")
    cypher_table = get_cypher_table(k1)
    df = pd.DataFrame([cypher_table])
    st.write(df)


if __name__ == "__main__":
    # render the app using streamlit ui function
    st_ui()
    # message = "Hello World!"
    # cypher_table = get_cypher_table(6)
    # print(cypher_table)
    # encrypted_msg = caesarCipher_encode(message, 6)
    # print(encrypted_msg)
    # decrypted_msg = caesarCipher_decode(encrypted_msg, 6)
    # print(decrypted_msg)
