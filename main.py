import os
import asyncio
import streamlit as st
from httpx_oauth.clients.google import GoogleOAuth2
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title = "SignUp", page_icon = "✍️", layout="wide")

def initialize_session_state():
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = ""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "user_email" not in st.session_state:
        st.session_state["user_email"] = ""

initialize_session_state()
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
redirect_uri = os.environ["REDIRECT_URI"]

if client_id and client_secret:
    client = GoogleOAuth2(client_id, client_secret)
else:
    client = None

async def get_authorization_url(client, redirect_uri):
    authorization_url = await client.get_authorization_url(redirect_uri, scope = ["profile", "email"])
    return authorization_url

async def get_access_token(client, redirect_uri, code):
    token = await client.get_access_token(code, redirect_uri)
    return token

async def get_email(client, token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email    


if client and st.session_state["authenticated"] == False:
    authorization_url = asyncio.run(get_authorization_url(client, redirect_uri))
    try:
        code = st.query_params()["code"]
    except:
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col7:
            st.write(f'''<h1> <a target="_self"href = "{authorization_url}"> Login </a> </h1>''', unsafe_allow_html = True)
    else:
        try:
            token = asyncio.run(get_access_token(client, redirect_uri, code))
        except:
            col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
            with col7:
                st.write(f'''<h1><a target="_self"href = "{authorization_url}"> Login </a> </h1>''', unsafe_allow_html = True)
                
        else:
            user_id, user_email = asyncio.run(get_email(client, token["access_token"]))
            st.session_state['user_id'] = user_id
            st.session_state['user_email'] = user_email
            st.session_state["authenticated"] = True
            
if st.session_state["authenticated"]:
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col7:
        if st.button("LogOut"):
            st.session_state["user_id"] = ""
            st.session_state["authenticated"] = False
            st.session_state["user_email"] = ""
            
welcome_message = ""
if st.session_state["user_email"]:
    welcome_message = "Welcome {}".format(st.session_state["user_email"])
    
col1, col2, col3, col4= st.columns(4)
with col4:
    st.write(welcome_message)