from keypoints import findnkp,savekeyPointsOnImage,kpForEqDist,kpForCenter
from entropy import calcEntropy
from pattern import Pattern 
import imgutil
import score
import json
import sys
import os

imagePath = sys.argv[1]
low = sys.argv[2]
feature = sys.argv[3]
intid = sys.argv[4]

low = str(low)+".jpg"
feature = str(feature)+".jpg"

# imagePath="result/pics/36.jpg"
# for i in range(1,39):
	# imagePath="result/pics/"+str(i)+".jpg"
	# print ("for =============",imagePath)

thr = 49
imgRgb = imgutil.imread(imagePath)
h,w = imgutil.imd(imgRgb)

# Save Orginal Image Resized 
imrs = imgutil.imresize(imgRgb,w,h)
imgutil.imwrite(low,imrs)
os.system("chmod 777  " + low)

#Save Gray Image Of KeyPoints
img = imgutil.rgb2gray(imgRgb)
imgrs = imgutil.imresize(img,w,h)
rh,rw = imgutil.imd(imgrs)
savekeyPointsOnImage(imgrs,feature,thr+16,rw,rh)
os.system("chmod 777  " + feature)

'''
1st ChechPoint 
Check for pattern within the image
'''
if Pattern(img,h,w):

	'''
	2nd ChechPoint 
	Chop the images into 4 equal half and get the keypoits
	'''
	kp,tlkp,trkp,blkp,brkp=kpForEqDist(img,thr,w,h)
	
	#Total Keypoints
#	print "total",kp
#	print "TopL",tlkp
#	print "TopR",trkp
#	print "BottomL",blkp
#	print "BottomR",brkp

	ckp, mkp, ekp = kpForCenter(img,thr,w,h)

#	print "center",ckp
#	print "mid",mkp
#	print "end",ekp

	#3rd ChechPoint 

	#4th ChechPoint
	ent = calcEntropy(img)
	
	a = score.ratingsForKeypoints(kp)
	b = score.ratingsForEqlDistOfKp(tlkp,trkp,blkp,brkp,kp,ckp,ekp)
	c = score.ratingsForEntropy(ent)

#	print '1st KP rating',a
#	print '2nd EQ rating',b
#	print '3rd EN rating',c

	#final CheckPoint 
	e = score.finalRating(a,b,c)

else:
	e = 0
#	print "It's Repetitive Pattern...!"

#print 'Final Rating : ',e

# Json Output
d={
'id':intid,
'height':h,
'weight':w,
'result':e
}
print(json.dumps(d)) 
