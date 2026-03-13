import unittest
from dab.account import *

class DABUnitTests(unittest.TestCase):
  def test_checkWithdrawal_A1(self):
    self.assertEqual(checkWithdrawal(600, 200), True)
  def test_checkWithdrawal_A2(self):
    self.assertEqual(checkWithdrawal(600, 600), False)
  def test_checkWithdrawal_A3(self):
    self.assertEqual(checkWithdrawal(300, 450), False)
  def test_checkWithdrawal_A4(self):
    self.assertEqual(checkWithdrawal(600, -3), False)

if __name__ == '__main__':
  unittest.main()
