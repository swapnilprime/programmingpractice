i=1  
a=[]  
b=[]  
for j in xrange(20):    
	for k in xrange(j):
		a.append(1)  
	if j>=3:  
	  for l in xrange(1,j-1):	  	
	  	a[l]=b[l-1]+b[l]  
	t = [str(i) for i in a]
	m=" ".join(t)
	print m.center(100)    
	b=a  
	a=[]  