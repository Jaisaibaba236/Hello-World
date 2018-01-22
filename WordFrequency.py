import string
import random
print(string.punctuation)

my_file = open("/home/inwkstudent/Desktop/testbook.txt")
dic = dict()
newdic = dict()
counter = 0

for line in my_file:
   global counter
   x = line.strip()
   for i in string.punctuation:
      line = line.replace(i,"")
   refined = line.split()
   for word in refined:
      dic[word] = random.random()
      counter += len(dic)
      if word in newdic:
          newdic[word] += 1
      else:
          newdic[word] = 1

print(len(dic))
print(newdic)
