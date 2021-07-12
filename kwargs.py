def func(**kwargs):
    print(kwargs)
    
    
func(firstname="kola",secondname="banana")
d={f"{i}":("even" if i%2==0 else "odd") for i in range(1,21) if i<15}
dd=dict.fromkeys("abcd","ünknown")
dictt={
      "name":"JOY",
      "age":23
}

func(**dictt)
func(**{"name":"kola","age":45})
func(**d)