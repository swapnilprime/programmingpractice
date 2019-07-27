#https://programmingpraxis.com/2011/01/07/counting-primes/
def isprime(n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2: 
		return True    
	if not n & 1: 
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

def primecount(n):
	cnt=0
	s = " "
	for i in range(1,n+1):
		#print isprime(i)
		if isprime(i) == True:
			#print i 
			s += str(i)+" " 
			cnt+=1
	print "Prime Numbers ",s
	print "Total Prime Numbers",cnt
	
def nthprime(n):
	cnt=1
	i=1
	while cnt!=n:
		if isprime(i):
			cnt+=1
		i+=1
	print n,"th prime no is",i-1  
while 1:
		try:
			ch=int(raw_input('\n1.Print Prime Numbers upto \n2.Print n-th Prime No \n3. Exit \n -->'))

			if ch==1:
				n=int(raw_input('Enter a Number-->'))
				primecount(n)
			elif ch==2:
				n=int(raw_input('Enter a Number-->'))
				nthprime(n)
			elif ch==3:
				print 'Bye Bye'
				exit()
			else:
				print 'Wrong Input'
		except:
			print 'Exception!!!'
			exit()
