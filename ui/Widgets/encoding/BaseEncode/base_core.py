import base64


def b64_encode(text: str):
    cipher = 'error base64'
    try:
        cipher = str(base64.b64encode(text.encode()).decode('utf-8'))
    except Exception:
        print('error base64')
        pass
    return cipher
    pass


def b64_decode(cipher: str):
    text = 'error base64'
    # 补齐为 4的倍数
    while len(cipher) % 4 != 0:
        cipher += '='
        pass
    try:
        text = str(base64.b64decode(cipher.encode()).decode('utf-8'))
        pass
    except Exception:
        print('error base64')
        pass
    return text
    pass


def b32_encode(text: str):
    cipher = 'error base32'
    try:
        cipher = str(base64.b32encode(text.encode()).decode('utf-8'))
    except Exception:
        print('error base32')
        pass
    return cipher
    pass


def b32_decode(cipher: str):
    text = 'error base32'
    # 补齐为 8的倍数
    while len(cipher) % 8 != 0:
        cipher += '='
        pass
    try:
        text = str(base64.b32decode(cipher.encode()).decode('utf-8'))
        pass
    except Exception:
        print('error base32')
        pass
    return text
    pass


def b16_encode(text: str):
    cipher = 'error base16'
    try:
        cipher = str(base64.b16encode(text.encode()).decode('utf-8'))
    except Exception:
        print('error base16')
        pass
    return cipher
    pass


def b16_decode(cipher: str):
    text = 'error base16'
    try:
        text = str(base64.b16decode(cipher.encode()).decode('utf-8'))
        pass
    except Exception:
        print('error base16')
        pass
    return text
    pass


# print(b64_encode('12345sssss'))
# print(b64_decode('MTIzNDUsss='))
# print(b32_encode("阿萨德"))
# print(b32_decode('5GML72EQVDS35NY=1'))
# print(b16_encode('12223数'))
# print(b16_decode('3132323233E695B0'))
