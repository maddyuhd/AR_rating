from imgutil import imread,imd,imresize,imwrite,cropTL,cropTR,cropBL,cropBR,rgb2gray
from score import ratingsForKeypoints,ratingsForEqlDistOfKp,ratingsForEntropy,finalRating
from keypoints import findnkp,savekeyPointsOnImage
from entropy import calcEntropy
from pattern import Pattern 
import json
import sys
import time

start =time.time()

# imagePath = sys.argv[1]
# for i in range(1,40):
# 	print i
# 	imagePath = "pics/"+str(i)+".jpg"
imagePath="test/10.jpg"
	# print imagePath

thr = 49

imgRgb = imread(imagePath)
h,w=imd(imgRgb)

# Orginal Image Resized 
imrs=imresize(imgRgb,w,h)
imwrite("res.jpg",imrs)

# Gray Image Of KeyPoints
img=rgb2gray(imgRgb)
imgrs=imresize(img,w,h)
rh,rw=imd(imgrs)
savekeyPointsOnImage(imgrs,"gray.jpg",thr+5,w,h)

#1st ChechPoint 

if Pattern(imgrs,rh,rw):
	pat=time.time()
	pat1=pat-start
	print "pat...time taken :",pat1
	
	# kp = findnkp(img,thr)

	#2nd ChechPoint 
	tl = cropTL(img,w,h)
	tr = cropTR(img,w,h)
	bl = cropBL(img,w,h)
	br = cropBR(img,w,h)

	tlkp=findnkp(tl,thr)
	trkp=findnkp(tr,thr)
	blkp=findnkp(bl,thr)
	brkp=findnkp(br,thr)

	#3rd ChechPoint 
	kp =tlkp+trkp+blkp+brkp

	#4th ChechPoint
	ent = calcEntropy(img)
	
	a = ratingsForKeypoints(kp)
	b = ratingsForEqlDistOfKp(tlkp,trkp,blkp,brkp,kp)
	c = ratingsForEntropy(ent)

	print '1st KP rating',a
	print '2nd EQ rating',b
	print '3rd EN rating',c

	#final CheckPoint 
	e = finalRating(a,b,c)

else:
	pat=time.time()
	pat1=pat-start
	print "Pattern...time taken :",pat1
	e = 0
	print "repetitive pattern..!!"

print 'Final Rating : ',e

#Json Output
d={
'user_id':e,
'photo_id':e,
'result':e}
print(json.dumps(d)) 
