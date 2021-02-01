thislist = ["a", "b", "c"]
thatlist = ["A", "B", "C"]

for j in thatlist:
   i = 0
   while i < len(thislist):
         if j ==  thislist[i].upper():
            print(thislist[i])
            i = i + 1
         else:
            i = i + 1
   print(j)
