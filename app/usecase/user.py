import os
from app.entity.user import User
from app.usecase.prompt import invalid_prompt, resp_prompt
from app.usecase.repo.user import create_account, authenticate
from app.usecase.repo.account import rp_deposit, rp_send_money, rp_withdraw

def sign_up():
  print("\n-------------------------------------------------\n")
  print("""Sign Up To Wafi Cash \n""")
  name = str(input("Enter Your name: "))
  print("\n")
  email = str(input("Enter Your Email: "))
  print("\n-------------------------------------------------\n")
  
  if resp_prompt() == 1:
    if create_account(email, name):
      return onboard_user()
    else:
      return sign_up()
  else:
    return onboard_user()


def login():
  print("\n-------------------------------------------------\n")
  print("""Login To Wafi Cash \n""")
  email = str(input("Enter Your Email: ")).lower()
  
  print("""\nTo Continue, Enter 1, To go Back, Enter Any Other Key""")
  res = int(input("Enter Prompt: "))
  print("\n-------------------------------------------------\n")
  if res == 1:
    print("signing in...")

    if authenticate(email) == True:
      return account_dashboard(email)
    else:
      print("Incorrect Login Credentials")
      print("\n-------------------------------------------------\n")
      print(
        """
        Welcome To Wafi Cash Terminal, Press: \n
        1. To Continue To Login Screen, 2. Go back to Home, Enter Any Other Key To Exit
        """
      )
      promptInput = int(input())
      if promptInput == 1:
        return login()
      elif promptInput == 2:
        return onboard_user()
  else:
    return

def onboard_user():
  print("\n-------------------------------------------------\n")
  print(
    """Welcome To Wafi Cash Terminal, Press: \n
    1. To Create An Account \n 
    2. To Login to your Account \n \n
    Enter Any Other Key To Exit
    """
  )
  promptInput = int(input())

  if promptInput == 1:
    sign_up()
  elif promptInput == 2:
    login()
  else:
    return os._exit(0)

def account_dashboard(email: str):
  print("\n-------------------------------------------------\n")
  user_data = User(email)
  print("""Welcome {name}🧑🏼‍🦱 To Your Wafi Dashboard, Enter \n""".format(name=user_data.getName()))
  print(
    """\n
    1. To Deposit Money
    2. To Send Money
    3. To See Available Balance
    4. To Withdraw
    5. To Logout \n
    """
  )

  print("\n-------------------------------------------------\n")

  response = str(input("Enter Prompt: "))
  if response == "1":
    print("\n-------------------------------------------------\n")
    print("""Deposit Cash💰 To Your Wafi Account \n""")
    amount = float(input("Enter Amount To Deposit: "))

    if resp_prompt() == 1:
      print("\n-------------------------------------------------\n")
      rp_deposit(email, amount)
      return account_dashboard(email)
    else:
      return account_dashboard(email)
  elif response == "2":
    print("\n-------------------------------------------------\n")

    print("""Send Money To Your Wafi Pal""")
    amount = float(input("Enter Amount To Send: "))
    recipient = str(input("Enter Recipient Email: "))

    print("\n-------------------------------------------------\n")
    if resp_prompt() == 1:
      if rp_send_money(email, amount, recipient):
        return account_dashboard(email)
      else:
        return account_dashboard(email)
    else:
      return account_dashboard(email)
  elif response == "3":
    print("\n-------------------------------------------------\n")
    user = User(email)
    print("------Your Account Balance💵 Is {balance} USD-------".format(balance=user.balance))
    res = input("Enter Any Key To Go Back: ")
    return account_dashboard(email)
  elif response == "4":
    print("\n-------------------------------------------------\n")
    print("""Withdraw Money From Your Wafi Wallet\n""")
    amount = float(input("Enter Amount To Withdraw: "))

    if resp_prompt() == 1:
      if rp_withdraw(email, amount):
        return account_dashboard(email)
      else:
        print("\n-------------------------------------------------\n")
        print("{} USD Withdrawal Falied: Insufficient Wallet Balance🚫\n".format(amount))
        return account_dashboard(email)
    else:
      return account_dashboard(email)

  elif response == "5":
    return onboard_user()
  else:
    invalid_prompt()
    return account_dashboard(email)