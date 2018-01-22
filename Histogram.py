s = 'banana'
histogram = {}

for i in s:
  if i in histogram:
     histogram[i] +=1
  else:
     histogram[i] = 1

print(histogram)
