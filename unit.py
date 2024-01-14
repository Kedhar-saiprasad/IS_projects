import unittest
import D:\\Software Engineering\\Project\\SERSA.py as SERSA

class TestEncrypt(unittest.TestCase):

	def test_encrypt(self):
		result=SERSA.encrypt("venkat")
		self.assertIsNot(result,"venkat")

if __name__=='__main__':
	unittest.main()