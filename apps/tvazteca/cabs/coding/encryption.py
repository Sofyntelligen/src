import base64
from Crypto.Cipher import AES


# https://repl.it/HzUW/1

class Encryption:
    key_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    key = "3DLbZdJ5XzIH6l1toInBp31Y1ahkOt0="
    block = 16
    displacement = 3
    iv = '\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'

    def __init__(self):
        self.data = ''

    def setBase64Encoded(self, ascii="utf-8"):
        data = base64.b64encode(self.data.encode(ascii))
        encoded = ''
        if len(data) > 0:
            for x in data:
                number = self.key_string.index(chr(x)) + self.displacement
                if number > len(self.key_string):
                    number -= len(self.key_string)
                encoded += self.key_string[number]
            return encoded
        return encoded

    def getBase64Encoded(self, ascii="utf-8"):
        date = ''
        encoded = ''
        if len(self.data) > 0:
            for x in self.data:
                number = self.key_string.index(x) - self.displacement
                if number < 0:
                    number += len(self.key_string)
                date += self.key_string[number]
        date = base64.b64decode(date.encode(ascii))
        for x in date:
            encoded += chr(x)
        return encoded

    def getkey_encryption(self):
        character = dict(enumerate(self.key))
        byte = []
        key_real = ''
        for position, char in character.items():
            byte.append(ord(char))
        for x in [1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97, 105, 113, 121]:
            key_real += chr(byte[int((x / 8) % len(byte))])
        return key_real

    def getEncryption(self):
        encoded = ''
        self.key = self.getkey_encryption()
        self.key = self.key.ljust(16, '\0')
        pad = self.block - (len(self.data) % self.block)
        date_encryption = self.data + chr(pad) * pad
        AES.key_size = 128
        encryptor = AES.new(key=self.key, mode=AES.MODE_CBC, IV=self.iv)
        encrypto = encryptor.encrypt(date_encryption)
        encrypto = base64.b64encode(encrypto)
        for x in encrypto:
            encoded += chr(x)
        return encoded

    def setData(self, data: str):
        self.data = data

    def getData(self):
        return self.data
