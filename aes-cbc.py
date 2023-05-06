import Crypto.Cipher.AES
import Crypto.Random
import base64
import binascii


class Cipher_AES:
	pad_default = lambda x, y: x + (y - len(x) % y) * " ".encode("utf-8")
	unpad_default = lambda x: x.rstrip()
	pad_user_defined = lambda x, y, z: x + (y - len(x) % y) * z.encode("utf-8")
	unpad_user_defined = lambda x, z: x.rstrip(z)
	pad_pkcs5 = lambda x, y: x + (y - len(x) % y) * chr(y - len(x) % y).encode("utf-8")
	unpad_pkcs5 = lambda x: x[:-ord(x[-1])]

	def __init__(self, key="abcdefgh12345678", iv=Crypto.Random.new().read(Crypto.Cipher.AES.block_size)):
		self.__key = key
		self.__iv = iv

	def set_key(self, key):
		self.__key = key

	def get_key(self):
		return self.__key

	def set_iv(self, iv):
		self.__iv = iv

	def get_iv(self):
		return self.__iv

	def Cipher_MODE_ECB(self):
		self.__x = Crypto.Cipher.AES.new(self.__key.encode("utf-8"), Crypto.Cipher.AES.MODE_ECB)

	def Cipher_MODE_CBC(self):
		self.__x = Crypto.Cipher.AES.new(self.__key.encode("utf-8"), Crypto.Cipher.AES.MODE_CBC,
										 self.__iv.encode("utf-8"))

	def encrypt(self, text, cipher_method, pad_method="", code_method=""):
		if cipher_method.upper() == "MODE_ECB":
			self.Cipher_MODE_ECB()
		elif cipher_method.upper() == "MODE_CBC":
			self.Cipher_MODE_CBC()
		cipher_text = b"".join([self.__x.encrypt(i) for i in self.text_verify(text.encode("utf-8"), pad_method)])
		if code_method.lower() == "base64":
			return base64.encodebytes(cipher_text).decode("utf-8").rstrip()
		elif code_method.lower() == "hex":
			return binascii.b2a_hex(cipher_text).decode("utf-8").rstrip()
		else:
			return cipher_text.decode("utf-8").rstrip()

	def decrypt(self, cipher_text, cipher_method, pad_method="", code_method=""):
		if cipher_method.upper() == "MODE_ECB":
			self.Cipher_MODE_ECB()
		elif cipher_method.upper() == "MODE_CBC":
			self.Cipher_MODE_CBC()
		if code_method.lower() == "base64":
			cipher_text = base64.decodebytes(cipher_text.encode("utf-8"))
		elif code_method.lower() == "hex":
			cipher_text = binascii.a2b_hex(cipher_text.encode("utf-8"))
		else:
			cipher_text = cipher_text.encode("utf-8")
		return self.unpad_method(self.__x.decrypt(cipher_text).decode("utf-8"), pad_method)

	def text_verify(self, text, method):
		while len(text) > len(self.__key):
			text_slice = text[:len(self.__key)]
			text = text[len(self.__key):]
			yield text_slice
		else:
			if len(text) == len(self.__key):
				yield text
			else:
				yield self.pad_method(text, method)

	def pad_method(self, text, method):
		if method == "":
			return Cipher_AES.pad_default(text, len(self.__key))
		elif method == "PKCS5Padding":
			return Cipher_AES.pad_pkcs5(text, len(self.__key))
		else:
			return Cipher_AES.pad_user_defined(text, len(self.__key), method)

	def unpad_method(self, text, method):
		if method == "":
			return Cipher_AES.unpad_default(text)
		elif method == "PKCS5Padding":
			return Cipher_AES.unpad_pkcs5(text)
		else:
			return Cipher_AES.unpad_user_defined(text, method)


def main2(msg, token):
	st_arr = []
	dy_arr = []
	static_str = 'Mu8weQyDvq1HlAzN'
	for b in bytearray(static_str, "utf-8"):
		st_arr.append(b)

	token_str = token[-16:]
	for b in bytearray(token_str, "utf-8"):
		dy_arr.append(b)

	res_byts = []
	for bt in bytes(a ^ b for (a, b) in zip(st_arr, dy_arr)):
		res_byts.append(bt)

	key = bytes(res_byts).decode()
	iv = key
	text = msg  # "7977099688"
	cipher_method = "MODE_CBC"
	pad_method = "PKCS5Padding"
	code_method = "base64"
	cipher_text = Cipher_AES(key, iv).encrypt(text, cipher_method, pad_method, code_method)
	cipher_text = cipher_text.replace('\n', '')
	print('[' + cipher_text + ']')
	print(type(cipher_text))
	text = Cipher_AES(key, iv).decrypt(cipher_text, cipher_method, pad_method, code_method)
	print(text)


if __name__ == '__main__':
	main2("405862999990475",
		  "CI6MTU3ODQ4ODYyM30.SAjMKd0chcAWoFwMkfxJ-Z1lWRM9-AeSXuHZiXBTYyo")