# 🏦 Bank Management System

A simple Banking Management System built using Python and Streamlit.

This project allows users to create bank accounts, deposit money, withdraw money, check balances, update account details, and delete accounts. Account data is stored locally using a JSON database.

---

## 🚀 Features

### Account Management
- Create a new account
- Automatic 12-digit account number generation
- Age verification (18+ only)
- Secure 4-digit PIN validation

### Banking Operations
- Deposit money
- Withdraw money
- Check account balance
- View account details

### Account Maintenance
- Update name, email, and PIN
- Delete account permanently

### Data Storage
- Persistent storage using JSON
- Data remains saved after application restart

---

## 📂 Project Structure

```text
Bank-Management-System/
│
├── app.py              # Streamlit Web Application
├── bank_main.py        # Python CLI Application
├── data.json           # Database File
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python 3
- Streamlit
- JSON
- Random
- String
- Pathlib

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/bank-management-system.git
cd bank-management-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or

```bash
pip install streamlit
```

---

## ▶️ Running the Streamlit App

```bash
streamlit run app.py
```

After running, open:

```text
http://localhost:8501
```

---

## ▶️ Running the Command Line Version

```bash
python bank_main.py
```

---

## 💾 Sample Database

```json
[
  {
    "name": "John Doe",
    "age": 22,
    "email": "john@example.com",
    "pin": 1234,
    "accountNo": "123456789012",
    "balance": 5000
  }
]
```

---

## 🔒 Validation Rules

### Account Creation
- Minimum age: 18 years
- PIN must be exactly 4 digits

### Deposit
- Maximum deposit: ₹100,000

### Withdrawal
- Maximum withdrawal: ₹100,000
- Cannot withdraw more than available balance

---

## 📸 Streamlit Interface

Features available through the web interface:

- Create Account
- Deposit Money
- Withdraw Money
- Check Balance
- Show Details
- Update Details
- Delete Account

---

## 🔮 Future Improvements

- User Login/Logout System
- Transaction History
- Dashboard Analytics
- CSV Statement Download
- PDF Statement Download
- Password Encryption
- Admin Panel
- Database Integration (SQLite/MySQL)
- Email Notifications

## 👨‍💻 Author

Som Shukla

Python Developer | Streamlit Enthusiast
