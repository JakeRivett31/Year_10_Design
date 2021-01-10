
sumofFactors = 0

def findFactors(number):
	factors = [1]
	for i in range(2, number//2 + 1):
		if (number % i == 0):
			factors.append(i)
	return factors		

def sumFactors(factors):
	sumofFactors = 0
	for i in range(0, len(factors)):
		sumofFactors += factors[i]
	return sumofFactors

def checkNumber(sumofFactors, number):
	
	if (sumofFactors == number):
		
		print(number)
		

for i in range(2, 10001):
	factors = findFactors(i)
	sumofFactors = sumFactors(factors)
	checkNumber(sumofFactors, i)
print("finished")













