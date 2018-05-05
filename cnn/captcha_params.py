numbers = [0,1,2,3,4,5,6,7,8,9]

MAX_CAPTCHA = 4
WIDTH = 160 
HEIGHT = 60

import string #randomly select characters
import random 
print(random.choice(string.ascii_letters)) 
#asll ascii letters:
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

def get_char_set():
	print("return :",str(string.digits)+string.ascii_letters)
	return (str(string.digits)+string.ascii_letters)

def get_width():
	return WIDTH
def get_height():
	return HEIGHT

def get_captcha_size():
	return MAX_CAPTCHA