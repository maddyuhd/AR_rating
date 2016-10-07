import cv2
from imgutil import imresize,imwrite

def findnkp(image, thr):
	fast = cv2.FastFeatureDetector_create(thr)
	kp = fast.detect(image,None)
	size=len(kp)
	print "Number of kp :",size
	return size;

def drawkeyPointsOnImage(image ,thr):
	fast = cv2.FastFeatureDetector_create(thr)
	kp = fast.detect(image,None)
	img2 = cv2.drawKeypoints(image, kp,None, color=(255,0,0))
	cv2.imshow('dst_rt', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return;
	
def savekeyPointsOnImage(image,imname ,thr,w,h):
	fast = cv2.FastFeatureDetector_create(thr)
	kp = fast.detect(image,None)
	img = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
	for k in kp:
		x,y=k.pt
		cv2.line(img, (int(x)-2,int(y)), (int(x)+2,int(y)),(0,255,255),1)
		cv2.line(img, (int(x),int(y)+2), (int(x),int(y)-2),(0,255,255),1)
	imwrite(imname,img)
	return;