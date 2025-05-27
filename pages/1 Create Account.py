import streamlit as st
from account import Account

if "accounts" not in st.session_state:
    st.session_state["accounts"] = []
if "bank_transactions" not in st.session_state:
    st.session_state["bank_transactions"] = []

st.title("👤 Create a New Account")

name = st.text_input("Name")
father_name = st.text_input("Father Name")
id_number = st.number_input("National ID", step=1)
ph_number = st.number_input("Mobile Number", step=1)
pin = st.text_input("Enter PIN", type="password")
pin2 = st.text_input("Confirm PIN", type="password")
initial_balance = st.number_input("Initial Deposit", step=1)

if pin != pin2:
    st.warning("❌ PINs do not match!")
elif len(str(pin)) != 4:
    st.warning("❌ PIN must be 4 digits!")
elif len(str(ph_number)) != 10:
    st.warning("❌ Phone number must be 10 digits!")
elif len(str(id_number)) != 12:
    st.warning("❌ ID number must be 13 digits!")
else:
    if st.button("Create Account"):
        new_acc = Account(id_number, ph_number, name, father_name, pin, initial_balance)
        st.session_state["accounts"].append(new_acc)
        st.success(f"✅ Account Created for {name}! Acc Number: {ph_number}")
