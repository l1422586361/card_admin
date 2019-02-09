import ast

file  = open("LIST")
# text = file.read()
# print(text[:-2])
list = []
# p = eval(text[:-2])
# list.append(p)
# print(list)



while True:
    text = file.readline()
    if not text:
        break
    list.append(ast.literal_eval(text)) # 使用eval会有安全问题，ast.literal_eval则不会
    print(text)
print(list)



file.close()

