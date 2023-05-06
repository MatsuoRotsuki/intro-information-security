import binascii
import os
import hashlib

from Crypto.Cipher import AES
from Crypto.Util import Counter


def convert_string2int(string):
    """
    Convert string to int format
    :param string: string of utf-8 format
    :return: hexlified string of int format
    """

    return int(binascii.hexlify(string), 16)


def encrypt_message(key, plain_text):
    """
    Encrypt message using AES CTR Mode
    :param key: key for encrypt
    :param plain_text: message to encrypt
    :return: initial vector, encrypted message
    """

    iv = os.urandom(16)  # Set Random value to initial vector
    ctr = Counter.new(128, initial_value=convert_string2int(iv))  # Set initial vector
    key = hashlib.sha3_224(key.encode('utf-8')).hexdigest()[0:32]  # Make length of key to 32 using SHA-3
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)  # Set CTR Mode to AES
    return iv, aes.encrypt(plain_text)


def decrypt_message(key, iv, cipher_text):
    """
    Decrypt message using AES CTR Mode
    :param key: key for decrypt
    :param iv: initial vector for AES encrypt
    :param cipher_text: encrypted message
    :return: utf-8 format string of decrypted message
    """

    ctr = Counter.new(128, initial_value=convert_string2int(iv))  # Set initial vector
    key = hashlib.sha3_224(key.encode('utf-8')).hexdigest()[0:32]  # Make length of key to 32 using SHA-3
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)  # Also, Set CTR Mode to AES
    return aes.decrypt(cipher_text).decode("utf-8")
