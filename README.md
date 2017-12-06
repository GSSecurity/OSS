# 암호화된 문자를 사진에 넣는 "steganography"

**라이센스:**  ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 지원 확장자

- JPG
- GIF
- PNG
- BMP
- ICO

## 미지원 확장자

- PDF

## 설치법

1. git clone을 통해 파일을 다운로드 받는다.
2. OSS/Stegano 파일로 이동 후 , python manage.py runserver로 Django를 구동시킨다.
3. 127.0.0.1:8000(Default 값)로 접속하여 암호화, 복호화 작업을 수행한다.
   (Safari를 이용할경우 이미지이름.png.html의 형태로 받아지는 경우가 있습니다.)

## 예제 사진

### 입력_사진

![input](https://github.com/GSSecurity/steganography/blob/merryman/sample/Stallman.jpg?raw=true)

### 출력_사진

![input](https://github.com/GSSecurity/steganography/blob/merryman/sample/Stallman_out.jpg?raw=true)

## CLI 예제 명령어

```python
# encode example: 사진에 문자열을 숨김
>>>steganography -e 입력_사진_경로 출력_사진_경로 문자열 암호키
>>>steganography -e input.png output.png 'HelloWorld' 'GSS'

# decode example: 사진으로 부터 숨겨진 문자열을 읽음
>>>steganography -d 출력_사진_경로 암호키(일치하지 않으면 디코딩 안됨)
>>>steganography -d output.png 'GSS'
숨겨 놓은 "문자열" 출력
```

## CLI 예제 코드

```python
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

## 웹 페이지 화면

http://gss.jaeil.wiki

### 암호화 페이지

![input](http://cfile10.uf.tistory.com/image/99F557335A27F4B2222D76)

### 복호화 페이지

![input](http://cfile30.uf.tistory.com/image/99F53D335A27F4B03986B0)