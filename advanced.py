l=["kalam","abu","solaiman","jaguar"]

print(max(l,key=len))

print(max(l,key=lambda a:len(a)))


l=[
  {"name":"JOY","score":90,"position":"8th"},
  {"name":"SAKIB","score":86,"position":"9th"},
  {"name":"RAKIB","score":96,"position":"2nd"}
  ]

print(max(l,key=lambda item:item.get("score")))


d={
   "joy":{"age":23},
   "abu":{"age":34},
   "kalam":{"age":44},
   "mohan":{"age":24},
   "salman":{"age":31}
  }

print(max(d,key=lambda a:d[a]['age']))
print(max(d,key=lambda a:d.get(a).get('age')))
print(d.get(max(d,key=lambda a:d[a]['age'])).get('age'))
print("Sorted Dictionary")
print(sorted(d,key=lambda a:d[a]['age']))
print(sorted(d,key=lambda a:d[a]['age'],reverse=True))
k=sorted(d,key=lambda a:d[a]['age'])
print(d[k[0]])