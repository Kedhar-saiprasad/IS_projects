import unittest
import SERSA

class TestEncrypt(unittest.TestCase):

	def test_encrypt(self):
		result=SERSA.encrypt((50, 3233),"venkat")
		self.assertIsNot(result,"venkat")

	def test_decrypt(self):
		result=SERSA.decrypt((125, 3233),[2821, 154, 2018, 2810, 2906, 1759])
		self.assertEqual(result,"venkat")
if __name__=='__main__':
	unittest.main()