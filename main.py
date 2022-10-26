
# ******************************
# Make your Code
# ******************************
import random

numbers1 = []
numbers2 = []
result = []
for i in range(10):
	rand1 = random.randint(0,100)
	rand2 = random.randint(0,100)
	total = rand1 + rand2
	numbers1.append(rand1)
	numbers2.append(rand2)
	result.append(total)
print (numbers1)
print (numbers2)
print(result)
