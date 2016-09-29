import numpy as np
import cv2
import math

def findNumberofkeypoints(image, thr):
	fast = cv2.FastFeatureDetector_create(thr)
	kp = fast.detect(image,None)
	size=len(kp)
	# print "Number of kp",size
	return size;

def drawkeyPointsOnImage(image ,thr):
	fast = cv2.FastFeatureDetector_create(thr)
	kp = fast.detect(image,None)
	img2 = cv2.drawKeypoints(image, kp,None, color=(255,0,0))
	#cv2.imwrite("fast_thr = "+str(thr)+", kp= "+ str(kp) +".jpg",img2)
	cv2.imshow('dst_rt', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return;

def resizeImage(image, w, h):
	img = cv2.resize(image, (w, h)) 
	return img;

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

def calcEntropy(img):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist = hist.ravel()/hist.sum()
    # print "test",len(hist)
    logs = np.log2(hist+0.00001)
    entropy = -1 * (hist*logs).sum()
    #print "Entropy Value :",entropy
    return entropy  

def finalRating(a, b, c):
	avg = math.ceil((a+b+c)/3.0 )
	return avg;

def ratingsForKeypoints(kp):
    
    if 0 <= kp <= 149:
    	return 0
    elif 150 <= kp <= 249:
    	return 1
    elif 250 <= kp <= 299:
    	return 2
    elif 300 <= kp <= 599:
    	return 3
    elif 600 <= kp <= 899:
    	return 4
    else:
		return 5

def ratingsForEntropy(en):
    
    if 0.0 <= en <= 3.0:
    	return 0
    elif 3.0 <= en <= 4.0:
    	return 1
    elif 4.0 <= en <= 5.0:
    	return 2
    elif 5.0 <= en <= 6.0:
    	return 3
    elif 6.0 <= en <= 7.0:
    	return 4
    elif en >=7.0:
    	return 5

def ratingsForEqlDistOfKp(TLkp, TRkp, BLkp, BRkp, kp):
    
    print"Total Kp",kp
    avgKp = kp /4
    print 'Average Kp',avgKp

    InitialCutoff=25 #For 0 Ratings
    cutoffFive =60
    cutoffFour =75
    cutoffThree =90
    cutoffTwo =95
   
    forFiveBelow = avgKp-((avgKp)*cutoffFive/100)
    forFiveAbove = avgKp+((avgKp)*cutoffFive/100)
    print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forFiveBelow,forFiveAbove)	
	
    forFourBelow = avgKp-((avgKp)*cutoffFour/100)
    forFourAbove = avgKp+((avgKp)*cutoffFour/100)
    print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forFourBelow,forFourAbove)	
	
    forThreeBelow = avgKp-((avgKp)*cutoffThree/100)
    forThreeAbove = avgKp+((avgKp)*cutoffThree/100)
    print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forThreeBelow,forThreeAbove)	
	
    forTwoBelow = avgKp-((avgKp)*cutoffTwo/100)
    forTwoAbove = avgKp+((avgKp)*cutoffTwo/100)
    print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forTwoBelow,forTwoAbove)	
	
    if avgKp >= InitialCutoff:
    	if (forFiveBelow <= TLkp <= forFiveAbove and
     forFiveBelow <= TRkp <= forFiveAbove and 
     forFiveBelow <= BLkp <= forFiveAbove and 
     forFiveBelow <= BRkp <= forFiveAbove):
    	   	return 5

    	elif (forFourBelow <= TLkp <= forFourAbove and
     forFourBelow <= TRkp <= forFourAbove and 
     forFourBelow <= BLkp <= forFourAbove and 
     forFourBelow <= BRkp <= forFourAbove):
    		return 4
    	elif (forThreeBelow <= TLkp <= forThreeAbove and
     forThreeBelow <= TRkp <= forThreeAbove and 
     forThreeBelow <= BLkp <= forThreeAbove and 
     forThreeBelow <= BRkp <= forThreeAbove):
    		return 3
    	elif (forTwoBelow <= TLkp <= forTwoAbove and
     forTwoBelow <= TRkp <= forTwoAbove and 
     forTwoBelow <= BLkp <= forTwoAbove and 
     forTwoBelow <= BRkp <= forTwoAbove):
    		return 2
    	else:
    		return 1
    else:
    		return 0

def notaPatter(img):
    
    if 2==3:
    	return False 
    else:
		return True


#imagePath = sys.argv[1]
img = cv2.imread("19.jpeg",2)#imagePath,2)#
(h,w) = img.shape[:2]
thr = 49

#initial CheckPoint For Patterns
if notaPatter(thr):
	
	#1st ChechPoint 
	kp = findNumberofkeypoints(img,thr)
	a=ratingsForKeypoints(kp)

	# drawkeyPointsOnImage(img,thr)
	print 'kp rating',a

	#2nd ChechPoint 
	tl = cropTopLeft(img,w,h)
	tr = cropTopRight(img,w,h)
	bl = cropBottomLeft(img,w,h)
	br = cropBottomRight(img,w,h)

	tlkp=findNumberofkeypoints(tl,thr)
	trkp=findNumberofkeypoints(tr,thr)
	blkp=findNumberofkeypoints(bl,thr)
	brkp=findNumberofkeypoints(br,thr)

	b = ratingsForEqlDistOfKp(tlkp,trkp,blkp,brkp,kp)

	print 'eq rating',b

	#3rd ChechPoint
	ent = calcEntropy(img)
	c = ratingsForEntropy(ent)
	print 'en rating',c
	name = 'Result kp = {}, eqlDisRating= {} , ent = {} .jpg'.format(kp,b,ent)	
	#cv2.imwrite(name,img)

	#drawkeyPointsOnImage(img,thr)	

	#final CheckPoint 
	e = finalRating(a,b,c)
else:
	e = 0
	print "The image contains repetitive pattern"

print 'Final rating : ',e
