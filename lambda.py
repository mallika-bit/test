people = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "cho", "house": "ravenclaw"},
    {"name": "draco", "house": "slytherin"}
]
list =['css','html','java','django']
#def f(person):
    #return person["house"]
sub = "ja"
newli = []
for li in list:
    if sub in li:
       #print("items found") 
       #print(li)
         newli.append(li)

print("results found")         

     
   
     
    

people.sort(key= lambda person: person["name"])

print(people)