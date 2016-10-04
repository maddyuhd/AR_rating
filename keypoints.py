import cv2

def findNumberofkeypoints(image, thr):
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
	
def savekeyPointsOnImage(image ,thr):
	fast = cv2.FastFeatureDetector_create(thr)
	kp = fast.detect(image,None)
	img2 = cv2.drawKeypoints(image, kp,None, color=(255,0,0))
	kpsize=len(kp)
	cv2.imwrite("IMG_thr = "+str(thr)+"_kp= "+ str(kpsize) +".jpg",img2)
	return;