a={"RAM":100,"HANUMAN":200,"LAXMAN":300,"SITA":400,"SHUBH":500}
print(a,type(a))
print(a["SHUBH"],a["RAM"])  
print(a.items())
print(a.keys())
print(a.values())
a.update({"RAM":10000, "HANUMAN":20000,"VIBHISHAN":1000})
print(a)
a["RAM"]=10000
print(a["RAM"])
print(a.get("HARRY"))
# print(a("HARRY"))  # This will give error
# print(a.get("HARRY","NOT FOUND"))
print(a)
print(a.pop(    "RAM"))
print(a)
print(a.popitem()) # This will remove last item
print(a)
