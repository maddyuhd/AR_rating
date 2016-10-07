import numpy as np

def Pattern(img,h,w):
	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)
	magnitude_spectrum = 20*np.log(np.abs(fshift))

	for num in range(250,w,10):
		z= zip(*np.where(magnitude_spectrum >= num))

		if len(z)<150:
			a= zip(*np.where(magnitude_spectrum >= num))
			c= abs(a[0][0]-h/2)
			print "patt = {}".format(c)
			if c<25:
				return True
			else:
				return False
