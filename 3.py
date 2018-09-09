# Problem 3
n = 100123192318236
factors = []
while n > 1:
	m = n**0.5
	is_prime = True	
	for i in range(2,int(m)):
		if n%i == 0:
			is_prime = False
			n = n/i
			factors.append(i)
	if is_prime:
		factors.append(n)
		break
factors.sort()		
print factors