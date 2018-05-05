from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt         # show captcha
from PIL import Image
import random
import os
import captcha_params
import string 

#string.ascii_letters are abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

def random_text(characters=captcha_params.get_char_set(),captcha_size= captcha_params.get_captcha_size()):
		captcha_text = []
		for i in range(captcha_size):
			char = random.choice(characters)
			captcha_text.append(str(char))

		captchaTextNoSpace = ''.join(captcha_text)
				
		print('no space')
		print(captchaTextNoSpace)
		return captchaTextNoSpace

def gen_captcha_text_and_image(iter):


	image=ImageCaptcha(width=captcha_params.get_width(), height = captcha_params.get_height(), font_sizes=[30])
	#print(image)
	captcha_text = random_text()
	path = '../images/' #go up one directory then create images folder

	if os.path.exists(path) == False: # if the folder is not existed, create it
		os.mkdir(path)            
	captcha = image.generate(captcha_text)
	print('c: ',captcha)
	# naming rules: num(in order)+'_'+'captcha text'.include num is for avoiding the same name
	image.write(captcha_text, path+str(iter)+'_'+captcha_text + '.png') 
	 
	captcha_image = Image.open(captcha)
	captcha_image = np.array(captcha_image)
		
	return captcha_text, captcha_image
	 
if __name__ == '__main__':

        #generates 20 samples
        for i in range(20): #change 20 to 20 000     
                text, image = gen_captcha_text_and_image(i)
                #view image
                #f = plt.figure()
                #f.canvas.set_window_title(text+'.png')
                #f.suptitle(text+'.png')
                #ax = f.add_subplot(111)
                #ax.text(0.1, 0.9,text, ha='center', va='center', transform=ax.transAxes)
                #plt.imshow(image)
                #plt.show()
      