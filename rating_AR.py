from keypoints import findnkp,savekeyPointsOnImage
from entropy import calcEntropy
from pattern import Pattern 
import imgutil
import score
import json
import sys

# imagePath = sys.argv[1]
# for i in range(1,40):
# 	print i
# 	imagePath = "pics/"+str(i)+".jpg"
imagePath="test/10.jpg"
	# print imagePath

thr = 49

imgRgb = imgutil.imread(imagePath)
h,w = imgutil.imd(imgRgb)

# Orginal Image Resized 
imrs = imgutil.imresize(imgRgb,w,h)
imgutil.imwrite("res.jpg",imrs)

# Gray Image Of KeyPoints
img = imgutil.rgb2gray(imgRgb)
imgrs = imgutil.imresize(img,w,h)
rh,rw = imgutil.imd(imgrs)
savekeyPointsOnImage(imgrs,"gray.jpg",thr+5,rw,rh)

#1st ChechPoint 
if Pattern(imgrs,rh,rw):

	#2nd ChechPoint 
	tl,tr,bl,br = imgutil.crop(img,w,h)

	tlkp=findnkp(tl,thr)
	trkp=findnkp(tr,thr)
	blkp=findnkp(bl,thr)
	brkp=findnkp(br,thr)

	#3rd ChechPoint 
	kp =tlkp+trkp+blkp+brkp

	#4th ChechPoint
	ent = calcEntropy(img)
	
	a = score.ratingsForKeypoints(kp)
	b = score.ratingsForEqlDistOfKp(tlkp,trkp,blkp,brkp,kp)
	c = score.ratingsForEntropy(ent)

	print '1st KP rating',a
	print '2nd EQ rating',b
	print '3rd EN rating',c

	#final CheckPoint 
	e = score.finalRating(a,b,c)

else:
	e = 0
	print "It's Repetitive Pattern...!"

print 'Final Rating : ',e

#Json Output
d={
'user_id':e,
'photo_id':e,
'result':e}
print(json.dumps(d)) 