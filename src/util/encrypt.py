import base64
import random
import time

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding


def generate_unique():
    a = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    o = [''] * 36
    o[8] = o[13] = o[18] = o[23] = "-"
    o[14] = "4"
    for n in range(36):
        if not o[n]:
            i = random.randint(0, 15)
            o[n] = a[3 & i | 8 if n == 19 else i]
    t = ''.join(o).replace('-', '')
    n = str(int(time.time() * 1000))
    return t + "+" + n


class Encrypt:
    def __init__(self, pub_key_content):
        pub_key = '-----BEGIN PUBLIC KEY-----\n' + pub_key_content + '\n-----END PUBLIC KEY-----'
        self.public_key = serialization.load_pem_public_key(pub_key.encode())

    def encrypt_long(self, string: str):
        bits = [0]
        byte_no = 0
        length = len(string)
        temp = 0
        ct = ''
        for i in range(length):
            ascii_code = ord(string[i])
            if 0x010000 <= ascii_code <= 0x10FFFF:
                byte_no += 4
            elif 0x000800 <= ascii_code <= 0x00FFFF:
                byte_no += 3
            elif 0x000080 <= ascii_code <= 0x0007FF:
                byte_no += 2
            else:
                byte_no += 1
            if byte_no % 117 >= 114 or byte_no % 117 == 0:
                if byte_no - temp >= 114:
                    bits.append(i)
                    # temp = hex2b64(byte_no)
        if len(bits) > 1:
            for i in range(len(bits) - 1):
                if i == 0:
                    str_sub = string[0: bits[i + 1] + 1]
                else:
                    str_sub = string[bits[i] + 1: bits[i + 1] + 1]
                ct += self.encrypt(str_sub)
            if bits[len(bits) - 1] != len(string) - 1:
                str_last = string[bits[len(bits) - 1] + 1]
                ct += self.encrypt(str_last)
            return ct
        return self.encrypt(string)

    def encrypt(self, string: str):
        return base64.b64encode(self.public_key.encrypt(string.encode(), padding.PKCS1v15())).decode()

    def generate_unique_encrypt(self):
        return self.encrypt_long(generate_unique())
