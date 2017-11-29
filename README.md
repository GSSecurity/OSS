# 암호화된 문자를 사진에 넣는 "steganography"

## 지원 확장자 (추가 확인)

GIF, BMP.

- JPG
- ICO
- PNG

##  미지원 확장자 (추가 확인)

- PDF

## 설치법

``` 
추후에 어떤식으로 할지 결정
```

## 예제 사진

### 입력_사진

{<div style="text-align:center;">
    ![input](https://github.com/GSSecurity/steganography/blob/merryman/sample/Stallman.jpg?raw=true)
  </div>}

### 출력_사진

![input](https://github.com/GSSecurity/steganography/blob/merryman/sample/Stallman_out.jpg?raw=true){.align-center}

## 예제 명령어

``` Python
# encode example: 사진에 문자열을 숨김
>>>steganography -e 입력_사진_경로 출력_사진_경로 문자열

# decode example: 사진으로 부터 숨겨진 문자열을 읽음
>>>steganography -d 출력_사진_경로
숨겨 놓은 "문자열" 출력
```

## 예제 코드

``` python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography

print "-*- hide text to image -*-"
path = "/Users/ryuminsu/Documents/GitHub/steganography/sample/Stallman.jpg"
output_path = "/Users/ryuminsu/Documents/GitHub/steganography/sample/Stallman_out.jpg"
text = 'Hello, this is testing code'
Steganography.encode(path, output_path, text)


print "-*- read secret text from image -*-"
secret_text = Steganograpy.decode(output_path)
print secret_text
```
