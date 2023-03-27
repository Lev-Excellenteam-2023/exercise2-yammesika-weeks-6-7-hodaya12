from PIL import Image

"""

:param param1: this is the path to the image
:returns: the decrypted message
"""
def decrypt_cipher(path):
    im = Image.open(path)
    im=im.convert('RGB')
    width, height=im.size
    pixles = im.load()
    message=''
    for i in range(width):
        for j in range(height):
            if pixles[i,j] == (1,1,1):
                message+=chr(j)
    return message

print(decrypt_cipher(r"code.png"))