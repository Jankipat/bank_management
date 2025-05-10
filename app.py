import streamlit as st
from hello import Bank

st.title("🏦 Bank Management System")

menu = [
    "Create Account", "Deposit Money", "Withdraw Money", 
    "View Details", "Update Details", "Delete Account"
]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Create Account":
    st.header("Open a New Bank Account")
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=0)
    email = st.text_input("Enter Email")
    pin = st.text_input("Set 4-digit Pin", type="password")
    if st.button("Create"):
        if name and email and pin:
            success, msg = Bank.create_account(name, int(age), email, int(pin))
            st.success(msg) if success else st.error(msg)

elif choice == "Deposit Money":
    st.header("Deposit")
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        success, msg = Bank.deposit(acc, int(pin), amount)
        st.success(msg) if success else st.error(msg)

elif choice == "Withdraw Money":
    st.header("Withdraw")
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        success, msg = Bank.withdraw(acc, int(pin), amount)
        st.success(msg) if success else st.error(msg)

elif choice == "View Details":
    st.header("View Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")
    if st.button("Show Details"):
        user = Bank.authenticate(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("No matching account found.")

elif choice == "Update Details":
    st.header("Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current Pin", type="password")
    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New 4-digit Pin (optional)", type="password")
    if st.button("Update"):
        success, msg = Bank.update_details(acc, int(pin), new_name, new_email, new_pin)
        st.success(msg) if success else st.error(msg)

elif choice == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("Pin", type="password")
    confirm = st.checkbox("I want to delete my account")
    if st.button("Delete") and confirm:
        success, msg = Bank.delete_account(acc, int(pin))
        st.success(msg) if success else st.error(msg)

