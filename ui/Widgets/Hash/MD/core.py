# import hashlib
from Cryptodome.Hash import MD2, MD4, MD5

def md5_32(string: str):
    # return hashlib.md5(string.encode(encoding='UTF-8')).hexdigest()
    return MD5.new(string.encode("utf8")).hexdigest()


def md5_16(string: str):
    return md5_32(string)[8:-8]


def md2(string: str):
    return MD2.new(string.encode("utf8")).hexdigest()


def md4(string: str):
    return MD4.new(string.encode("utf8")).hexdigest()

if __name__ == "__main__":
    s = 'aaassf'
    print(md5_32(s))
    print(md5_16(s))
    print(md2(s))
    print(md4(s))
    pass