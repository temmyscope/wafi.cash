from app.config.config import USER_DATABASE

def create_account(email: str, name: str) -> bool:
  pass

def authenticate(email: str) -> bool:
  if email in USER_DATABASE:
    return True
  else:
    return False