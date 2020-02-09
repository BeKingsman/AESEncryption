from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 16
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
encode = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
decode = lambda c, e: c.decrypt(base64.b64decode(e)).decode("UTF-8").rstrip(PADDING)
secret = os.urandom(BLOCK_SIZE)
cipher = AES.new(secret)
