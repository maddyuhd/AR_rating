import cv2
import imgutil
import keypoints
import entropy
import score


def notaPatter(img):
    
    if 2==3:
    	return False 
    else:
		return True


#imagePath = sys.argv[1]
imagePath = "pics/4.jpg"

img = cv2.imread(imagePath,2)
(h,w) = img.shape[:2]
thr = 49

#initial CheckPoint For Patterns
if notaPatter(thr):
	
	#1st ChechPoint 
	kp = keypoints.findNumberofkeypoints(img,thr)
	a=score.ratingsForKeypoints(kp)

	# drawkeyPointsOnImage(img,thr)
	print 'KP rating',a

	#2nd ChechPoint 
	tl = imgutil.cropTopLeft(img,w,h)
	tr = imgutil.cropTopRight(img,w,h)
	bl = imgutil.cropBottomLeft(img,w,h)
	br = imgutil.cropBottomRight(img,w,h)

	tlkp=keypoints.findNumberofkeypoints(tl,thr)
	trkp=keypoints.findNumberofkeypoints(tr,thr)
	blkp=keypoints.findNumberofkeypoints(bl,thr)
	brkp=keypoints.findNumberofkeypoints(br,thr)

	b = score.ratingsForEqlDistOfKp(tlkp,trkp,blkp,brkp,kp)

	print 'EQ rating',b

	#3rd ChechPoint
	ent = entropy.calcEntropy(img)
	c = score.ratingsForEntropy(ent)
	print 'EN rating',c

	#final CheckPoint 
	e = score.finalRating(a,b,c)

else:
	e = 0
	print "The image contains repetitive pattern"

print 'Final rating : ',e
