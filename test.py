import unittest
from app.usecase.repo.user import create_account, authenticate
from app.usecase.repo.account import rp_deposit, rp_send_money, rp_withdraw


class TestUserAndAccountRepos(unittest.TestCase):

  def test_all_handlers(self):
    #Test Account Creation: Should be true when "Account Does Not Exists"
    self.assertTrue( create_account("sample@yahoo.com", "Random User 0") )
    self.assertTrue( create_account("user1@yahoo.com", "Random User 1") )
    #Test Account Creation: Should be false when "Account Exists"
    self.assertFalse( create_account("sample@yahoo.com", "Random Name") )

    #Test Authenticate: Should be true when "Account Exists"
    self.assertTrue( authenticate("sample@yahoo.com") )
    #Test Authenticate: Should be false when "Account Does Not Exists"
    self.assertFalse( authenticate("sample@gm.com") )

    #Test Deposit Fund: Should be True when "Account Exists"
    self.assertTrue( rp_deposit("sample@yahoo.com", 20) )
    #Test Deposit Fund: Should be False when "Account Does Not Exists"
    self.assertFalse( rp_deposit("sample2@yahoo.com", 20) )

    #Test Withdrawal: Should be True when "Fund Is Sufficient"
    self.assertTrue( rp_withdraw("sample@yahoo.com", 5) )
    #Test Withdrawal: Should be False when "Fund Is Insufficient"
    self.assertFalse( rp_withdraw("sample@yahoo.com", 25) )
    
    #Test Send Money: Should be True when "Fund Is Sufficient"
    self.assertTrue( rp_send_money("sample@yahoo.com", 7.5, "user1@yahoo.com") )
    #Test Send Money: Should be False when "Recipient Does Not Exist"
    self.assertFalse( rp_send_money("sample@yahoo.com", 20, "user2@yahoo.com") )
    #Test Send Money: Should be False when "Fund Is Insufficient"
    self.assertFalse( rp_send_money("sample@yahoo.com", 20, "user1@yahoo.com") )

if __name__ == '__main__':
  unittest.main()