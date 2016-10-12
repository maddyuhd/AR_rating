import cv2

def imread(img):
	img = cv2.imread(img,1)
	return img;

def imd(img):
	(h,w) = img.shape[:2]
	return (h,w);

def imresize(image, w, h):
	ar=w/float(h)
	if h>w:
		ar=w/float(h)
		newH=320
		newW=int(newH*ar)
	else:
		ar=h/float(w)
		newW=320
		newH=int(newW*ar)
		
	img = cv2.resize(image, (newW, newH)) 
	return img;
	
def imwrite(imagename,img2):
	cv2.imwrite(imagename,img2)
	return ;
	
def rgb2gray(img):
	imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	return imgGray;

def gray2rgb(img):
	imgRgb = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
	return imgRgb;

def drawLines(image, x, y):
	# cv2.line(image, (int(x)-2,int(y)), (int(x)+2,int(y)),(0,255,255),1)
	return ;

def crop(image, w, h):
	imgTL = image[0:h/2, 0:w/2] 
	imgTR = image[0:h/2, w/2:w] 
	imgBL = image[h/2:h, 0:w/2]
	imgBR = image[h/2:h, w/2:w] 
	return imgTL,imgTR,imgBL,imgBR;