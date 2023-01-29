from app.config.config import USER_DATABASE

class User:
  name: str
  email: str
  balance: float

  def __init__(self, email: str):
    user_data = USER_DATABASE[email]
    if email in USER_DATABASE:
      self.email = email
      self.name = user_data["name"]
      self.balance = user_data["balance"]
    else:
      raise Exception("User Does not Exist")

  def getName(self):
    return self.name

  def getBalance(self):
    return self.balance