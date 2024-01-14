import unittest
import Func

class TestEncrypt(unittest.TestCase):

	def test_encrypt(self):
		result1=Func.encrypt((3233, 1273),"venkat")
		result2=Func.encrypt((3233, 511),"sai prasad")
		result3=Func.encrypt((3233, 3023),"rishitha")
		result4=Func.encrypt((3233, 1867),"sai thej")
		result5=Func.encrypt((3233, 1393),"sohan")
		self.assertIsNot(result1,[118, 101, 110, 107, 97, 116])
		self.assertIsNot(result2,[115, 97, 105, 32, 112, 114, 97, 115, 97, 100])
		self.assertIsNot(result3,[114, 105, 115, 104, 105, 116, 104, 97])
		self.assertIsNot(result4,[115, 97, 105, 32, 116, 104, 101, 106])
		self.assertIsNot(result5,[115, 111, 104, 97, 110])

	def test_decrypt(self):
		result1=Func.decrypt((3233, 1897),[1506, 3212, 1683, 1326, 736, 917])
		result2=Func.decrypt((3233, 751),[1654, 890, 688, 1188, 559, 2570, 890, 1654, 890, 1137])
		result3=Func.decrypt((3233, 2927),[525, 1218, 1203, 1250, 1218, 2292, 1250, 493])
		result4=Func.decrypt((3233, 1123),[1787, 598, 3020, 1005, 2250, 1161, 875, 2120])
		result5=Func.decrypt((3233, 2737),[555, 538, 2982, 187, 1256])
		self.assertEqual(result1,"venkat")
		self.assertEqual(result2,"sai prasad")
		self.assertEqual(result3,"rishitha")
		self.assertEqual(result4,"sai thej")
		self.assertEqual(result5,"sohan")


if __name__=='__main__':
	unittest.main()