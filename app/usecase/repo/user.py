from app.config.config import USER_DATABASE

def create_account(email: str, name: str) -> bool:
  print("\n-------------------------------------------------\n")
  print("validating...\n")
  if email in USER_DATABASE:
    print("\n-------------------------------------------------\n")
    print("An Account with that email already exists")
    return False
  else:
    print("\n-------------------------------------------------\n")
    USER_DATABASE[email] = {"balance": 0, "name": name, "email": email}
    print("Account Created...\n")
    return True

def authenticate(email: str) -> bool:
  if email in USER_DATABASE:
    return True
  else:
    return False