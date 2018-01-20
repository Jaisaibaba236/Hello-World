def gcd(x,y):
   gcd_number = 0
   if x>y:
       min = y
       max = x
   else:
       min = x
       max = y
   counter = 1
   while counter<min:
      if min%counter == 0 and max%counter == 0:
         gcd_number = counter
      counter = counter+1
   return gcd_number
      

print(gcd(28,56))
