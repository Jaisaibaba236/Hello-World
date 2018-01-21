listing = [1,1,1,1,[1,1,1,[1,1],1,1]]
sum = 0

def nested_sum(listing):
   global sum  
   for i in listing:
      if type(i) == int:
        sum += i
      else:
        nested_sum(i)
   return sum

print(nested_sum(listing))
