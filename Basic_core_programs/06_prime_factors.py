import math
def primeFactors(n):
	
	while n % 2 == 0: #this loop applies till n will be odd number
		print(2)
		n = n // 2 
	for i in range(3,int(math.sqrt(n))+1,2): #here it increment +2 because we dont need even numbers again
		while n % i== 0:
			print(i)
			n = n // i
			
	# Condition if n is a prime, Number greater than 2
	if n > 2:
		print(n)
		
#inputs
n = 315
primeFactors(n)
