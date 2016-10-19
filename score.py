import math

def finalRating(a, b, c):
    if a == b and (c >= a+2 or c >= a-2) :
        print "case 1"
        return a

    elif b == c and (a >= b+2 or a >= b-2):
        print "case 2"
        return b

    elif a == c and (b >= a+2 or b >= a-2) :
        print "case 3"
        return c
    
    else :
        avg = math.ceil((a+b+c)/3.0 )
        print "case 4"
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

def ratingsForEqlDistOfKp(TLkp, TRkp, BLkp, BRkp, kp,ckp, ekp):
    
    # print"Total Kp",kp
    avgKp = kp /4
    print 'Average Kp',avgKp

    InitialCutoff=25 #For 0 Ratings
    cutoffFive =60
    cutoffFour =75
    cutoffThree =90
    cutoffTwo =95
   
    forFiveBelow = avgKp-((avgKp)*cutoffFive/100)
    forFiveAbove = avgKp+((avgKp)*cutoffFive/100)
    # print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forFiveBelow,forFiveAbove)	
	
    forFourBelow = avgKp-((avgKp)*cutoffFour/100)
    forFourAbove = avgKp+((avgKp)*cutoffFour/100)
    # print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forFourBelow,forFourAbove)	
	
    forThreeBelow = avgKp-((avgKp)*cutoffThree/100)
    forThreeAbove = avgKp+((avgKp)*cutoffThree/100)
    # print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forThreeBelow,forThreeAbove)	
	
    forTwoBelow = avgKp-((avgKp)*cutoffTwo/100)
    forTwoAbove = avgKp+((avgKp)*cutoffTwo/100)
    # print 'is {} ,{} ,{} and {} between {} - {} ?'.format(TLkp,TRkp,BLkp,BRkp,forTwoBelow,forTwoAbove)	
	
    if avgKp >= InitialCutoff:
        if (forFiveBelow <= TLkp <= forFiveAbove and forFiveBelow <= TRkp <= forFiveAbove and forFiveBelow <= BLkp <= forFiveAbove and 
     forFiveBelow <= BRkp <= forFiveAbove):
            if ckp<ekp:
                return 4
            else:
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