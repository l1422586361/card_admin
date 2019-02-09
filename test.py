import ast
f = open("LIST")
list=[]
list2={'name': 'lin', 'phone': '123', 'email': '123'}
while True:
    a = f.readline()
    if not a:
        break
    list.append(ast.literal_eval(a))
print(list)

for dict in list:
    if dict["name"] == "lin":
        list.remove(dict)
        list.append(list2)
print(list)
f = open("LIST","w")
f.truncate()
for dict in list:
    f = open("LIST","a+")
    # f.seek(0)
    f.write(str(dict)+"\n")


    # print(dict)

# f.write(str(list))
# f.writelines(str(list))



f.close()