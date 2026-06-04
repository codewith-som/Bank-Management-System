import streamlit as st
import json
import random
import string
from pathlib import Path

# -----------------------------
# Bank Class
# -----------------------------
class Bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
    except Exception:
        data = []

    @staticmethod
    def update():
        with open(Bank.database, "w") as fs:
            json.dump(Bank.data, fs, indent=4)

    @classmethod
    def generate_account_number(cls):
        while True:
            acc = "".join(random.choices(string.digits, k=12))
            exists = any(i["accountNo"] == acc for i in cls.data)

            if not exists:
                return acc

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18:
            return False, "Age must be 18 or above."

        if len(pin) != 4 or not pin.isdigit():
            return False, "PIN must be exactly 4 digits."

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo": cls.generate_account_number(),
            "balance": 0
        }

        cls.data.append(account)
        cls.update()

        return True, account

    @classmethod
    def find_user(cls, account_no, pin):
        for user in cls.data:
            if user["accountNo"] == account_no and user["pin"] == int(pin):
                return user
        return None


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Bank Management System", page_icon="🏦")

st.title("🏦 Bank Management System")

menu = st.selectbox(
    "Choose Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Check Balance",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)

# -----------------------------
# Create Account
# -----------------------------
if menu == "Create Account":

    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):

        success, result = Bank.create_account(
            name, age, email, pin
        )

        if success:
            st.success("Account Created Successfully!")

            st.write("### Account Details")
            st.write(f"**Name:** {result['name']}")
            st.write(f"**Account Number:** {result['accountNo']}")
            st.write(f"**Balance:** ₹{result['balance']}")
        else:
            st.error(result)

# -----------------------------
# Deposit
# -----------------------------
elif menu == "Deposit Money":

    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input(
        "Amount",
        min_value=1,
        step=1
    )

    if st.button("Deposit"):

        user = Bank.find_user(acc, pin)

        if not user:
            st.error("Invalid account number or PIN.")

        elif amount > 100000:
            st.error("Maximum deposit limit is ₹100000.")

        else:
            user["balance"] += amount
            Bank.update()

            st.success("Amount Deposited Successfully")
            st.info(f"Current Balance: ₹{user['balance']}")

# -----------------------------
# Withdraw
# -----------------------------
elif menu == "Withdraw Money":

    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input(
        "Amount",
        min_value=1,
        step=1
    )

    if st.button("Withdraw"):

        user = Bank.find_user(acc, pin)

        if not user:
            st.error("Invalid account number or PIN.")

        elif amount > 100000:
            st.error("Maximum withdrawal limit is ₹100000.")

        elif amount > user["balance"]:
            st.error("Insufficient balance.")

        else:
            user["balance"] -= amount
            Bank.update()

            st.success("Amount Withdrawn Successfully")
            st.info(f"Current Balance: ₹{user['balance']}")

# -----------------------------
# Check Balance
# -----------------------------
elif menu == "Check Balance":

    st.subheader("Check Balance")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Check"):

        user = Bank.find_user(acc, pin)

        if not user:
            st.error("Invalid account number or PIN.")
        else:
            st.success(f"Current Balance: ₹{user['balance']}")

# -----------------------------
# Show Details
# -----------------------------
elif menu == "Show Details":

    st.subheader("Show Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):

        user = Bank.find_user(acc, pin)

        if not user:
            st.error("Invalid account number or PIN.")
        else:
            st.json(user)

# -----------------------------
# Update Details
# -----------------------------
elif menu == "Update Details":

    st.subheader("Update Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")

    if st.button("Load Account"):

        user = Bank.find_user(acc, pin)

        if user:
            st.session_state.user = user
        else:
            st.error("Invalid account number or PIN.")

    if "user" in st.session_state:

        user = st.session_state.user

        new_name = st.text_input(
            "New Name",
            value=user["name"]
        )

        new_email = st.text_input(
            "New Email",
            value=user["email"]
        )

        new_pin = st.text_input(
            "New PIN",
            value=str(user["pin"])
        )

        if st.button("Update"):

            if len(new_pin) != 4 or not new_pin.isdigit():
                st.error("PIN must be 4 digits.")

            else:
                user["name"] = new_name
                user["email"] = new_email
                user["pin"] = int(new_pin)

                Bank.update()

                st.success("Details Updated Successfully")

# -----------------------------
# Delete Account
# -----------------------------
elif menu == "Delete Account":

    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    confirm = st.checkbox(
        "I understand this action cannot be undone."
    )

    if st.button("Delete Account"):

        user = Bank.find_user(acc, pin)

        if not user:
            st.error("Invalid account number or PIN.")

        elif not confirm:
            st.warning("Please confirm deletion.")

        else:
            Bank.data.remove(user)
            Bank.update()

            st.success("Account Deleted Successfully")