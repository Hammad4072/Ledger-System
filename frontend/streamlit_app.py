import streamlit as st
import requests

BASE = "http://localhost:8000"

st.title("📒 Ledger System")

menu = ["Register", "Login", "Add Entry", "View Ledger"]
choice = st.sidebar.selectbox("Menu", menu)

if "token" not in st.session_state:
    st.session_state["token"] = None

if choice == "Register":
    st.subheader("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        r = requests.post(f"{BASE}/register", json={"username": username, "password": password})
        st.write(r.json())

if choice == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        r = requests.post(f"{BASE}/login", data={"username": username, "password": password})
        if "access_token" in r.json():
            st.session_state["token"] = r.json()["access_token"]
            st.success("Logged in")
        else:
            st.error("Login failed")

if choice == "Add Entry" and st.session_state["token"]:
    st.subheader("Add Ledger Entry")
    title = st.text_input("Title")
    amount = st.number_input("Amount")
    type_ = st.selectbox("Type", ["income", "expense"])
    if st.button("Add"):
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        r = requests.post(f"{BASE}/ledger/", json={"title": title, "amount": amount, "type": type_}, headers=headers)
        st.write(r.json())

if choice == "View Ledger" and st.session_state["token"]:
    st.subheader("Ledger Entries")
    headers = {"Authorization": f"Bearer {st.session_state['token']}"}
    r = requests.get(f"{BASE}/ledger/", headers=headers)
    if r.status_code == 200:
        for entry in r.json():
            st.write(entry)
