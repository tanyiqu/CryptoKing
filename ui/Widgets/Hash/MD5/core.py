# import hashlib
from Cryptodome.Hash import MD5


def md5_32(string: str):
    return MD5.new(string.encode("utf8")).hexdigest()
