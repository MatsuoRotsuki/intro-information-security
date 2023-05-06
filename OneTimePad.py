import binascii
def encrypt(cipher,plain,plain_want):
    int_plain = int(binascii.hexlify(bytes(plain, 'ascii')),16)
    int_plain_want = int(binascii.hexlify(bytes(plain_want, 'ascii')),16)
    int_cipher = int(binascii.a2b_qp(cipher),16)
    #print(int_plain)
    #print(int_plain_want)
    #print(int_cipher)
    int_key = int_plain ^ int_cipher
    return '{:x}'.format(int_key ^ int_plain_want),'{:x}'.format(int_key)


print(encrypt("6c73d5240a948c86981bc294","gui duc 100d","gui duc 321d"))
