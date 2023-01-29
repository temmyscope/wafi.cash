from app.usecase.user import onboard_user

#In an actual system, we would have a password
def open_wafi_cash_terminal():
  return onboard_user()

open_wafi_cash_terminal()