# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from lib.steganography import Steganography

print "-*- hide text to image -*-"
path = "/Users/ryuminsu/Documents/GitHub/SteganographyApp/sample/Stallman.jpg"
output_path = "/Users/ryuminsu/Documents/GitHub/SteganographyApp/sample/Stallman_out.jpg"
text = 'Hello, this is testing code'
Steganography.encode(path, output_path, text)


print "-*- read secret text from image -*-"
secret_text = Steganography.decode(output_path)
print secret_text
