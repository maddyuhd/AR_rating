import imgutil
import keypoints
import entropy
import score
import pattern

#imagePath = sys.argv[1]
imagePath = "pics/4.jpg"

thr = 49

img = imgutil.imread(imagePath)
h,w=imgutil.imagedimensions(img)

#initial CheckPoint For Patterns
if pattern.notaPatter(thr):
	
	#1st ChechPoint 
	kp = keypoints.findNumberofkeypoints(img,thr)
	a=score.ratingsForKeypoints(kp)

	# drawkeyPointsOnImage(img,thr)
	print '1st KP rating',a

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

	print '2nd EQ rating',b

	#3rd ChechPoint
	ent = entropy.calcEntropy(img)
	c = score.ratingsForEntropy(ent)
	print '3rd EN rating',c

	#final CheckPoint 
	e = score.finalRating(a,b,c)

else:
	e = 0
	print "The image contains repetitive pattern"

print 'Final rating : ',e
