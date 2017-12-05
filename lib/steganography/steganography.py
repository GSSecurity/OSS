# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import sys
from PIL import Image
import random
import hashlib
import os


DIST = 8

# this is secret key, just for you
# you have to input same secret key, when encode & decode image
# if it incorrect, you cannot decode image
def keyInput():

	secretKey = raw_input("Secret Key : ")
	print("You have inputed \"%s\" as a Secret Key" % secretKey)
	encryptedKey = hashlib.sha256()
	encryptedKey.update(secretKey)

	return encryptedKey.hexdigest()

### ENCODE
##### Functions about normalize() #####

def _normalize(i):

	if i >= 128:
		i -= 1
	else:
		i += 1

	return i

# is it normalize condition?
def is_modify_pixel(r, g, b):
	"""
	:param r: int
	:param g: int
	:param b: int
	:return: bool
	"""
	# check if r & g & b is multiples of 8(DIST) + 1
	# this is a characteristic of the modified pixel
	return r % DIST == g % DIST == b % DIST == 1

# if the modify condition is true, then do a normalize
def normalize_pixel(r, g, b):
	"""
	pixel color normalize
	:param r: int
	:param g: int
	:param b: int
	:return: (int, int, int)
	"""
	if is_modify_pixel(r, g, b):
		seed = random.randint(1, 3)
		if seed == 1:
			r = _normalize(r)
		if seed == 2:
			g = _normalize(g)
		if seed == 3:
			b = _normalize(b)

	return r, g, b

# modify a pixel to insert text
def normalize(input_path, output_path):
	"""
	normalize image
	:param input_path: str
	:param output_path: str
	"""
	img = Image.open(input_path)
	img = img.convert('RGB')

	# Image.size return tuple : (width, height) in pixel
	# size[0] : width, size[1] : height
	size = img.size
	new_img = Image.new('RGB', size)

	for y in range(img.size[1]):
		for x in range(img.size[0]):
			# get each r, g, b value
			r, g, b = img.getpixel((x, y))
			_r, _g, _b = normalize_pixel(r, g, b)
			new_img.putpixel((x, y), (_r, _g, _b))

	new_img.save(output_path, "PNG", optimize = True)

#######################################


##### Functions about hide_text() #####

def _modify(i):
	if i >= 128:
		for x in xrange(DIST + 1):
			if i % DIST == 1:
				return i
			i -= 1
	else:
		for x in xrange(DIST + 1):
			if i % DIST == 1:
				return i
			i += 1
	raise ValueError

def modify_pixel(r, g, b):
	"""
	pixel color modify
	:param r: int
	:param g: int
	:param b: int
	:return: (int, int, int)
	"""
	return map(_modify, [r, g, b])

def to_hex(s):
	return s.encode("hex")

# the process of hiding text in an image
def hide_text(output_path, hide_info):
	"""
	hide text to image
	:param output_path: str
	:param hide_info: str
	"""
	text = str(hide_info)

	# convert 'text(string)' to 'hex_value' for write
	write_param = []
	_base = 0

	for _ in to_hex(text):
		write_param.append(int(_, 16) + _base)
		_base += 16

	# hide hex-text to image
	img = Image.open(output_path)
	counter = 0
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			if counter in write_param:
				r, g, b = img.getpixel((x, y))
				r, g, b = modify_pixel(r, g, b)
				img.putpixel((x, y), (r, g, b))
			counter += 1

	img.putpixel((1, 1), 33)

	# save
	img.save(output_path, "PNG", optimize = True)

#######################################

### DECODE
##### Functions about read_text() #####

def to_str(s):
	return s.decode("hex")

# finding hidden text
def read_text(path):
	"""
	read secret text from image
	:param path: str
	:return: str
	"""
	img = Image.open(path)
	counter = 0
	result = []
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			r, g, b = img.getpixel((x, y))
			if is_modify_pixel(r, g, b):
				result.append(counter)
			counter += 1
			if counter == 16:
				counter = 0

	return to_str(''.join([hex(_)[-1:] for _ in result]))

#######################################

class Steganography(object):

	@classmethod
	def encode(cls, input_image_path, output_image_path, encode_text):
		"""
		hide text to image
		:param input_image_path: str
		:param output_image_path: str
		:param encode_text: str
		"""
		normalize(input_image_path, output_image_path)
		hide_text(output_image_path, encode_text)
		assert read_text(output_image_path) == encode_text, read_text(output_image_path)

	@classmethod
	def decode(cls, image_path):
		"""
		read secret text from image
		:param image_path: str
		:return: str
		"""
		return read_text(image_path)


# Main program
def main():
	available_list = ['jpg', 'gif', 'png', 'bmp', 'ico']

	# check file extension
	# handle exception with no extension
	try:
		signature = sys.argv[2].split('.')[1]
	except :
		print("There is no extension!!")
		return

	if not signature.lower() in available_list:
		print(signature + " is not supported extension!!")
		return

	secretCode = keyInput()
	secretCodeLength = len(secretCode)

	# when encode image
	# steganography -e input_image_path output_image_path hide_text
	if len(sys.argv) == 5 and sys.argv[1] == '-e':

		input_image_path = sys.argv[2]
		output_image_path = sys.argv[3]
		text = secretCode + sys.argv[4]

		imgCh = Image.open(input_image_path)

		# checksum
		### i think this code has problem...
		checkPixel = imgCh.getpixel((1, 1))
		if checkPixel == (33, 0, 0):
			print("Already encoded!!")
		###
		else:
			print("Start Encode : {}".format(input_image_path))
			Steganography.encode(input_image_path, output_image_path, text)
			print("Finish Encode : {}".format(output_image_path))
			print("Input Image Size : %d" % os.path.getsize(input_image_path))
			print("Output Image size : %d" % os.path.getsize(output_image_path))
			#the end of else(Line 215)
		return

	# when decode image
	# steganography -d output_image_path
	if len(sys.argv) == 3 and sys.argv[1] == '-d':
		# decode
		input_image_path = sys.argv[2]
		result = Steganography.decode(input_image_path)

		# check Secret Key
		leakSecretCode = result[0:secretCodeLength]
		if secretCode == leakSecretCode:
			print("Your secret message was \"%s\"" % result[secretCodeLength:])
		else:
			print("You are not permited!!")
		return

	# when the execution format is wrong
	print_help_text()

# help messages
def print_help_text():
	print("ERROR: not SteganographyApp command")
	print("--------------------------------")
	print("# encode example: hide text to image")
	print("SteganographyApp -e /tmp/image/input.jpg /tmp/image/output.jpg 'The quick brown fox jumps over the lazy dog.'")
	print("")
	print("# decode example: read secret text from image")
	print("SteganographyApp -d /tmp/image/output.jpg")
	print("")

if __name__ == "__main__":
	main()
