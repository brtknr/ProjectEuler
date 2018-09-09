# Problem 2
last = 1
this = 2
total = 0
while this < 4000000:
	if this%2 == 0:
		total += this
	print this,last
	last,this = this, this+last