from app.config.config import USER_DATABASE

def rp_deposit(email: str, amount: float) -> bool:
  print("\n-------------------------------------------------\n")
  if email not in USER_DATABASE:
    print("Current User Is Invalid")
    return False
  
  print("funding your account...\n")
  USER_DATABASE[email]["balance"] += amount 
  print("Accound🏦 Funded Successfully")
  return True

def rp_send_money(email: str, amount: float, recipient: str) -> bool:
  print("\n-------------------------------------------------\n")
  if email not in USER_DATABASE:
    print("Current User Is Invalid")
    return False
  if recipient not in USER_DATABASE:
    print("Recipient Does Not Exist")
    return False
  elif USER_DATABASE[email]["balance"] >= amount:
    print("Sending...")
    USER_DATABASE[email]["balance"] -= amount
    USER_DATABASE[recipient]["balance"] += amount
    print("{} Sent✅".format(amount))
    return True
  else:
    print("Insufficient Fund🚫")
    return False

def rp_withdraw(email: str, amount: float) -> bool:
  print("\n-------------------------------------------------\n")
  if email not in USER_DATABASE:
    print("Current User Is Invalid")
    return False
  elif USER_DATABASE[email]["balance"] >= amount:
    print("Withdrawing To Bank...")
    USER_DATABASE[email]["balance"] -= amount
    print("Withdrawal of {} USD Completed✅".format(amount))
    return True


