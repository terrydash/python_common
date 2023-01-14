import rsa

from config.startupconfig import init_config


def encrypt(content: str):
    content = rsa.encrypt(content.encode('utf-8'), init_config.rsa.publickey)
    #print(content)
    return content


def decrypt(content: bytes):
    content = rsa.decrypt(content, init_config.rsa.privatekey)
    content = content.decode('utf-8')
    #print(content)
    return content


from Cryptodome.Cipher import AES
from binascii import b2a_base64, a2b_base64


class Prpcrypt(object):
    def __init__(self, key):
        self.mode = AES.MODE_CBC
        self.key = self.pad_key(key)

    def pad(self, text):
        text = bytes(text, encoding="utf8")
        while len(text) % 16 != 0:
            text += b'\0'
        return text

    def pad_key(self, key):
        key = bytes(key, encoding="utf8")
        while len(key) % 16 != 0:
            key += b'\0'
        return key

    def encrypt(self, text):
        texts = self.pad(text)
        aes = AES.new(self.key, self.mode, self.key)
        res = aes.encrypt(texts)
        return str(b2a_base64(res), encoding="utf-8")

    def password_encrypt(self, text):
        return self.encrypt(self.encrypt(text))

    def password_decrypt(self, text):
        return self.decrypt(self.decrypt(text))

    def decrypt(self, text):
        texts = a2b_base64(self.pad(text))
        aes = AES.new(self.key, self.mode, self.key)
        res = str(aes.decrypt(texts), encoding="utf8").replace('\x00', '')
        return res


prpcrypt = Prpcrypt('xgxxgxxgxxgxxgxx')
