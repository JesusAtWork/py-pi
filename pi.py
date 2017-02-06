from decimal import *
piList = []
calcList = []
acc = -2
pi = 0
actual = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481"
iterations = 1000000
getcontext().prec = 50


def nilakantha():
	pi = Decimal(3)
	div = Decimal(2)
	for i in range(iterations):
		pi += 4 / (div * (div + 1) * (div + 2))
		div += 2
		pi -= 4 / (div * (div + 1) * (div + 2))
		div += 2
	return pi

def leibniz():
	pi = Decimal(0)
	div = Decimal(1)
	for i in range(iterations):
		pi += 4/div
		div += 2
		pi -= 4/div
		div += 2
	return pi

# pi = leibniz()
pi = nilakantha()

for i in str(pi):
	piList.append(i)
for i in str(actual):
	calcList.append(i)
for n,i in enumerate(piList):
	if n < len(calcList) and i == calcList[n]:
		acc += 1
	else: break

print("calculated: " + str(pi))
print("actual    : " + str(actual))
print("accurate to " + str(acc) + " decimal places")
print(str(iterations) + " iterations")