import cv2

def imread(img):
	img = cv2.imread(img,2)
	return img;

def imagedimensions(img):
	(h,w) = img.shape[:2]
	return (h,w);

def resizeImage(image, w, h):
	img = cv2.resize(image, (w, h)) 
	return img;
	
def imwrite(imagename,img2):
	cv2.imwrite(imagename,img2)
	return ;
	
def cropTopLeft(image, w, h):
	img = image[0:h/2, 0:w/2] 
	return img;

def cropTopRight(image, w, h):
	img = image[0:h/2, w/2:w] 
	return img;

def cropBottomLeft(image, w, h):
	img = image[h/2:h, 0:w/2]
	return img;

def cropBottomRight(image, w, h):
	img = image[h/2:h, w/2:w] 
	return img;