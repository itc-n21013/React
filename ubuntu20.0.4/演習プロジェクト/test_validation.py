from cnath import exp
import unittest
from validation import validatePassword

class Test_validation(unittest.TestCase):
    def test_validatePassword(self):
    actual = validatePassword(self):
    expected = 'バリデーションが完了しました。'
    actual = validatePassword('passwordA111')
    self.asserEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(5)