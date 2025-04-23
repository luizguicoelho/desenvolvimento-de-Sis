## a = arquivo; l = linha; ps = palavras

ps = []
a = open("ccomida.txt", "r") 
for l in a:
    ps.append(l.strip())



print(ps)    