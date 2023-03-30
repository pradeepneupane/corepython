def funargs(normal,*args,**kwargs):
    print(normal)
    for items in args:
        print(items)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

normal = "This is normal"
friends = ["Pradeep","sonam","Rasmi"]
kw = {"Pradeep":"DS","Sonam":"B","Rasmi":"CMA"}
funargs(normal,*friends,**kw)