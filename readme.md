## WAFI Cash Terminal (Code Assessment)

- Requirements: python3

### Set Up
```sh
git clone https://github.com/temmyscope/wafi.cash.git
```

### Run Code
```sh
python3 main.py
```

### Important Note
- In a real life application, `password` would be required for login

### Terminal Prompts (Onboarding)

```py
"""
Welcome To WAFI Cash Terminal
1. To Create Account
2. To Login to your Account
"""
```

### Terminal Prompts (Account - Logged In User)

```py
"""
Hello {{name}}, Enter

1. To Deposit Money
2. To Send Money
3. To See Available Balance
4. To Withdraw
5. To Logout
"""
```

### Run Tests
```sh
python3 -m unittest test.py
```