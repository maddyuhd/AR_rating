from keypoints import findnkp,savekeyPointsOnImage,kpForEqDist,kpForCenter
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
imagePath="test/6.jpg"

thr = 49
imgRgb = imgutil.imread(imagePath)
h,w = imgutil.imd(imgRgb)

# Save Orginal Image Resized 
imrs = imgutil.imresize(imgRgb,w,h)
imgutil.imwrite("low_res.jpg",imrs)

#Save Gray Image Of KeyPoints
img = imgutil.rgb2gray(imgRgb)
imgrs = imgutil.imresize(img,w,h)
rh,rw = imgutil.imd(imgrs)
savekeyPointsOnImage(imgrs,"feature_img.jpg",thr+5,rw,rh)

'''
1st ChechPoint 
Check for pattern within the image
'''
if Pattern(imgrs,rh,rw):

	'''
	2nd ChechPoint 
	Chop the images into 4 equal half and get the keypoits
	'''
	kp,tlkp,trkp,blkp,brkp=kpForEqDist(img,thr,w,h)
	

	
	#Total Keypoints
	# print "total",kp

	ckp, mkp, ekp = kpForCenter(img,thr,w,h)

	# print "center",ckp
	# print "mid",mkp
	# print "end",ekp

	#3rd ChechPoint 

	#4th ChechPoint
	ent = calcEntropy(img)
	
	a = score.ratingsForKeypoints(kp)
	b = score.ratingsForEqlDistOfKp(tlkp,trkp,blkp,brkp,kp,ckp,ekp)
	c = score.ratingsForEntropy(ent)

	# print '1st KP rating',a
	# print '2nd EQ rating',b
	# print '3rd EN rating',c

	#final CheckPoint 
	e = score.finalRating(a,b,c)

else:
	e = 0
	# print "It's Repetitive Pattern...!"

# print 'Final Rating : ',e

# Json Output
d={
'user_id':e,
'photo_id':e,
'result':e
}
print(json.dumps(d)) 